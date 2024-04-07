model_name = "distilbert-base-uncased"
tokenizer_name = "distilbert-base-uncased"
#batch_size = 26
num_epochs = 10

from sklearn.metrics import accuracy_score 
import json
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import Dataset, DataLoader
import torch
from torch.nn.utils.rnn import pad_sequence
import torch.nn as nn
import torch.nn.functional as F

class ReviewDataset(Dataset):
    def __init__(self, examples, labels, tokenizer):
        self.examples = examples
        self.labels = labels
        
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        example = self.examples[idx]
        label = self.labels[idx]

        # Tokenize the title and label
        inputs = self.tokenizer.encode_plus(
            example,
            add_special_tokens=True,
            padding="max_length",
            max_length=512,
            truncation=True,
            return_tensors="pt"
        )

        input_ids = inputs["input_ids"].squeeze()
        attention_mask = inputs["attention_mask"].squeeze()
        label_id = int(label) - 1

        return input_ids, attention_mask, torch.tensor(label_id)

def collate_fn(batch):
    input_ids, attention_masks, labels = zip(*batch)
    input_ids = pad_sequence(input_ids, batch_first=True)
    attention_masks = pad_sequence(attention_masks, batch_first=True)
    labels = torch.stack(labels)

    return input_ids, attention_masks, labels

def load_fasttext_data(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.read().splitlines()

    labels = []
    texts = []
    for line in lines:
        label, text = line.split(" ", 1)
        labels.append(label.replace('__label__', ''))
        texts.append(text)
    return labels, texts

class FocalLoss(nn.Module):
    def __init__(self, alpha=1, gamma=2):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, inputs, targets):
        ce_loss = F.cross_entropy(F.softmax(inputs, dim=-1), targets, reduction='none')
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha * (1 - pt) ** self.gamma * ce_loss

        return focal_loss.mean()

def train(batch_size):
#load datasets
    train_labels, train_examples = load_fasttext_data("train.ft.txt")
    test_labels, test_examples = load_fasttext_data("test.ft.txt")

    # Define the hyperparameter values to search
    alpha = 1
    gamma = 2

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

    dataset = ReviewDataset(train_examples, train_labels, tokenizer)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
    criterion = FocalLoss(alpha=alpha, gamma=gamma)

    validation_dataset = ReviewDataset(test_examples, test_labels, tokenizer)
    validation_data_loader = DataLoader(validation_dataset, batch_size=batch_size, collate_fn=collate_fn)

    patience = 2  # Number of epochs to wait for improvement in accuracy
    early_stopping_counter = 0  # Counter to keep track of epochs without improvement
    prev_accuracy = 0
    for epoch in range(num_epochs):
            total_loss = 0

            for i, (inputs, attention_mask, labels) in tqdm(enumerate(data_loader), total = len(data_loader)):
                inputs = inputs.to(device)
                attention_mask = attention_mask.to(device)
                labels = labels.to(device)

                outputs = model(inputs, attention_mask=attention_mask)
                loss = criterion(outputs.logits, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if i == len(data_loader)//2:
                    model.eval()
                    true_labels = []
                    predicted_labels = []

                    for inputs, attention_mask, labels in tqdm(validation_data_loader):
                        inputs = inputs.to(device)
                        attention_mask = attention_mask.to(device)
                        labels = labels.to(device)

                        with torch.no_grad():
                            outputs = model(inputs, attention_mask=attention_mask)
                            _, predicted = torch.max(outputs.logits, dim=1)

                            true_labels.extend(labels.tolist())
                            predicted_labels.extend(predicted.tolist())

                    accuracy = accuracy_score(true_labels, predicted_labels)
                    print(f"Step {i} - Validation Accuracy: {accuracy:.4f}")
                    model.train()


            avg_loss = total_loss / len(data_loader)
            print(f"Epoch {epoch+1} - Average Loss: {avg_loss:.4f}")

            # Calculate accuracy on validation data
            model.eval()
            true_labels = []
            predicted_labels = []

            for inputs, attention_mask, labels in tqdm(validation_data_loader):
                inputs = inputs.to(device)
                attention_mask = attention_mask.to(device)
                labels = labels.to(device)

                with torch.no_grad():
                    outputs = model(inputs, attention_mask=attention_mask)
                    _, predicted = torch.max(outputs.logits, dim=1)

                    true_labels.extend(labels.tolist())
                    predicted_labels.extend(predicted.tolist())

            accuracy = accuracy_score(true_labels, predicted_labels)
            print(f"Epoch {epoch+1} - Validation Accuracy: {accuracy:.4f}")

            # Check if accuracy improved
            if accuracy > prev_accuracy:
                early_stopping_counter = 0
                model.save_pretrained("BBv1")

            else:
                early_stopping_counter += 1

            # Check if early stopping criteria is met
            if early_stopping_counter >= patience:
                print("Early stopping triggered. No improvement in Accuracy.")
                break
            prev_accuracy = accuracy
    model.save_pretrained("BBv1")

if __name__ == "__main__":
    # Main function to classify reviews
    batch_size = int(input("Enter Batch Size"))
    train(batch_size)