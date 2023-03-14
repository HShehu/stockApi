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


@app.get("/getStock")
def getStock(stockSym : str):
    # find exact stock from file
    newstock = None
    stocks = json.load(open("./stocks.json"))
    for stock in stocks['stocks']:
        if stock['symbol'] == stockSym:
            newstock = stock
            break

    if newstock is None:
        return

    return newstock


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
            newstock['lastUpdate'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            stock = newstock
            print(stock)
            break

    if newstock is None:
        return

    # update document
    with open("./stocks.json", "w") as jsonFile:
        json.dump(stocks, jsonFile,indent=4,sort_keys=True)


@app.put("/sellStock")
def sellStock(stockSym : str , amount : int):
    # find exact stock from file
    newstock = None
    stocks = json.load(open("./stocks.json"))
    for stock in stocks['stocks']:
        if stock['symbol'] == stockSym:
            newstock = stock
            # add to number of shares
            newstock['availableShares'] += amount
            newstock['lastUpdate'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            stock = newstock
            print(stock)
            break

    if newstock is None:
        return

    # update document
    with open("./stocks.json", "w") as jsonFile:
        json.dump(stocks, jsonFile,indent=4,sort_keys=True)
