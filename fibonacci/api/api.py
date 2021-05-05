from typing import List

from fastapi import FastAPI

from db import database, Fibonacci
import schema

app = FastAPI(title='Fibonacci API')

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/fibonacci/{number}", response_model=schema.Fibonacci)
async def fibonacci(number: int):
    query = Fibonacci.select().where(Fibonacci.c.number == number)
    return await database.fetch_one(query)

@app.get("/fibonacci/sequence/{number}", response_model=List[schema.Fibonacci])
async def fibonacci(number: int):
    query = Fibonacci.select().where(Fibonacci.c.number <= number)
    return await database.fetch_all(query)