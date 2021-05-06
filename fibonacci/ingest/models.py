import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from dotenv import load_dotenv

from sqlite_foreign_keys import _set_sqlite_pragma

load_dotenv('.env')

postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
postgres_db = os.environ['POSTGRES_DB']
postgres_user = os.environ['POSTGRES_USER']
postgres_pass = os.environ['POSTGRES_PASS']

engine = create_engine(f'postgresql://{postgres_user}:{postgres_pass}@{postgres_host}:{postgres_port}/{postgres_db}', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Fibonacci(Base):
    
    __tablename__ = 'fibonacci'
    number = Column(Integer, primary_key=True)
    fibonacci_number = Column(String)
    fibonacci_history = relationship('FibonacciHistory', back_populates='fibonacci')

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.number}: {self.fibonacci_number})>'

    @classmethod
    def exists(cls, session: Session, number: int) -> bool:
        if session.query(Fibonacci).filter(Fibonacci.number == number).first():
            return True
        return False

class FibonacciHistory(Base):

    __tablename__ = 'fibonacci_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    fibonacci = relationship('Fibonacci', back_populates='fibonacci_history')
    number = Column(Integer, ForeignKey('fibonacci.number'))

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.number}: {self.date})>'

Base.metadata.create_all(bind=engine)