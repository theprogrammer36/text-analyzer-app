from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class Sentence(BaseModel):
    sentence: str


@app.post('/analyze')
def analyze(sentenceReference: Sentence):
    blob = TextBlob(sentenceReference.sentence)
    return blob.sentiment


@app.get('/')
def intro():
    return "Hello Shaik"
