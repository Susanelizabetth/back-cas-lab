# Bring in lightweight dependencies
import pickle

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def scoring_endpoint():
    return {"name": "hello world"}
