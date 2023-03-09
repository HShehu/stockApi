from http.client import HTTPException
from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from models import Stocks,Stock
from datetime import datetime
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/listStock" , response_model = Stocks)
def listStock():

    return json.load(open("./stocks.json"))

@app.put("/buyStock/{stockId}")
def buyStock(stockId : int , stock : Stock):
# find exact stock from file
    
# subtract number of shares
# update document
# return stock
            #return stock
    pass