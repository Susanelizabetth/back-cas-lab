# Bring in lightweight dependencies
import pickle

from functools import wraps

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import json
from cachetools import cached, TTLCache


app = FastAPI()
templates = Jinja2Templates(directory="templates")
origins = [
    "https://susanelizabetth.github.io",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScoringItem(BaseModel):
    albumina: float
    globulos_blancos: int
    creatinina: float
    hipertension: int
    diabetes_mellitus: float


class ScoringItems(BaseModel):
    List[ScoringItem]


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.post('/')
async def scoring_endpoint(item: List[ScoringItem]):
    data = []
    for i in item:
        data.append(i.dict())
    df = pd.DataFrame(data)
    yhat = model.predict(df)

    return {"prediction": yhat.tolist()}


@cached(cache=TTLCache(maxsize=1, ttl=60*60*48))
def get_json():
    df = pd.read_csv('data.csv')
    df.fillna(0)
    return json.loads(df.to_json(orient='records'))


@app.get('/')
async def get_data_csv():
    return get_json()
