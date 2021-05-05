import databases
import sqlalchemy

DATABASE_URL = 'postgresql://fibonacci:fibonacci@localhost:5432/fibonacci_sequence'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)

Fibonacci = sqlalchemy.Table('fibonacci', metadata, autoload_with=engine)