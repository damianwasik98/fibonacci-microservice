from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from sqlite_foreign_keys import _set_sqlite_pragma

engine = create_engine('postgresql://postgres:secret@localhost:5432/postgres', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Fibonacci(Base):
    
    __tablename__ = 'fibonacci'
    number = Column(String, primary_key=True)
    fibonacci_number = Column(String)
    fibonacci_history = relationship('FibonacciHistory', back_populates='fibonacci')

class FibonacciHistory(Base):

    __tablename__ = 'fibonacci_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    fibonacci = relationship('Fibonacci', back_populates='fibonacci_history')
    number = Column(String, ForeignKey('fibonacci.number'))

Base.metadata.create_all(bind=engine)