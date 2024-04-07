from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.responses import JSONResponse
import logging
import sys
from typing import Union

from text_classification.algo_manager import BERT, LSTM, Spacy
from text_classification.model import Sentiment, SentimentAnalysis, SentimentModel


app = FastAPI()


FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(stream=sys.stdout, format=FORMAT)
logger = logging.getLogger(__name__)


@app.post("/predict/{model}", response_model=SentimentAnalysis)
async def predict(model: SentimentModel,
                  file: UploadFile = File(...)) -> Union[SentimentAnalysis, JSONResponse]:
    try:
        text = (await file.read()).decode("utf-8")
        logger.warning(f"Uploaded text: {text} {type(text)}")

        return await predict(model, text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def predict(model: SentimentModel,
                  text: str) -> SentimentAnalysis:
    if model == SentimentModel.SPACY:
        model = Spacy()
    elif model == SentimentModel.BERT:
        ...
    elif model == SentimentModel.LSTM:
        ...

    return model.predict(text)

