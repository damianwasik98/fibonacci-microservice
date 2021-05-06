from typing import List

from fastapi import FastAPI, HTTPException

from db import database, Fibonacci
import schema

tags_metadata = [
    {
        "name": "fibonacci",
        "description": "Get fibonacci result for given number"
    },
    {
        "name": "fibonacci_sequence",
        "description": "Get fibonacci sequence from 0 to given number"
    }
]


app = FastAPI(title='Fibonacci API', openapi_tags=tags_metadata)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/fibonacci/{number}", response_model=schema.Fibonacci, tags=['fibonacci'])
async def fibonacci(number: int):
    query = Fibonacci.select().where(Fibonacci.c.number == number)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail='Fibonacci number not exists in database yet')
    else:
        return result 

@app.get("/fibonacci/sequence/{number}", response_model=List[schema.Fibonacci], tags=['fibonacci_sequence'])
async def fibonacci(number: int):
    query = Fibonacci.select().where(Fibonacci.c.number <= number)
    result = await database.fetch_all(query)
    if not result:
        raise HTTPException(status_code=404, detail='Fibonacci number not exists in database yet')
    else:
        return result 