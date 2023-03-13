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
    return {"msg": "Helloooo World"}

@app.get("/listStock" , response_model = Stocks)
def listStock():

    return json.load(open("./stocks.json"))

@app.put("/buyStock")
def buyStock(stockSym : str , amount : int):
# find exact stock from file
    newstock = None
    stocks = json.load(open("./stocks.json"))
    for stock in stocks['stocks']:
        if stock['symbol'] == stockSym:
            newstock = stock
            # subtract number of shares
            if (newstock['availableShares'] - amount) < 0:
                return
            newstock['availableShares'] -= amount
            stock = newstock
            print(stock)
            break

    if newstock is None:
        return

    with open("./stocks.json", "w") as jsonFile:
        json.dump(stocks, jsonFile,indent=4,sort_keys=True)


    
    
# update document

# return stock
    pass