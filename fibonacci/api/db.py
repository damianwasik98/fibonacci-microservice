import os

import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv('.env')

postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
postgres_db = os.environ['POSTGRES_DB']
postgres_user = os.environ['POSTGRES_USER']
postgres_pass = os.environ['POSTGRES_PASS']

DATABASE_URL = f'postgresql://{postgres_user}:{postgres_pass}@{postgres_host}:{postgres_port}/{postgres_db}'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)

Fibonacci = sqlalchemy.Table('fibonacci', metadata, autoload_with=engine)
