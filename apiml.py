# Bring in lightweight dependencies
import pickle

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


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
