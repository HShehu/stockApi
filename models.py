from pydantic import BaseModel,PastDate
from datetime import datetime

class Stock(BaseModel):
    name : str
    symbol : str
    availableShares : int
    currency : str
    price : float
    lastUpdate : datetime

class Stocks(BaseModel):
    stocks : list[Stock]


