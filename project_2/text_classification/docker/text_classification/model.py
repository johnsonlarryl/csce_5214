from enum import Enum
from pydantic import BaseModel


class Sentiment(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


class SentimentAnalysis(BaseModel):
    sentiment: Sentiment


class SentimentModel(Enum):
    BERT = "bert"
    SPACY = "spacy"
    LSTM = "lstm"
