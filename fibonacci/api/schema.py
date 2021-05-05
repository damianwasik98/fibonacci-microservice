from pydantic import BaseModel


class Fibonacci(BaseModel):
    number: int
    fibonacci_number: str