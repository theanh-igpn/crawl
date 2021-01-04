#!/usr/bin/python3

from pymongo import MongoClient

cars =  {'name': 'Audi', 'price': 52642}

client = MongoClient('mongodb://root:K5mvHk@35.240.237.82:27017/web2?authSource=admin')

with client:

    db = client.testdb
    print()
    db.cars.insert_one(cars)