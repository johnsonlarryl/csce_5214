from abc import ABC, abstractmethod
import os
import spacy
from typing import Dict


from text_classification.model import Sentiment, SentimentAnalysis


class Algo(ABC):
    @abstractmethod
    def load(self) -> object: pass

    @abstractmethod
    def predict(self, text: str) -> SentimentAnalysis: pass


class Spacy(Algo):
    def load(self) -> object:
        model_dir = self.get_model_dir()

        return spacy.load(model_dir)

    def predict(self, text: str) -> SentimentAnalysis:
        model = self.load()
        prediction = model(text).cats
        return self.get_sentiment(prediction)

    def get_model_dir(self):
        return os.path.join(os.path.dirname(__file__), "../spacy")

    def get_sentiment(self, prediction: [Dict[str, float]]):
        positive_sentiment = prediction[Sentiment.POSITIVE.value]
        negative_sentiment = prediction[Sentiment.NEGATIVE.value]

        if positive_sentiment > negative_sentiment:
            return SentimentAnalysis(sentiment=Sentiment.POSITIVE)
        else:
            return SentimentAnalysis(sentiment=Sentiment.NEGATIVE)


class BERT(Algo):
    ...


class LSTM(Algo):
    ...
