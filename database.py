#importing SQLalchemy tools

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#loadd envt varaiables from .env files
load_dotenv()

#database conncetion URL- tells pyton where to find your database

DATABASE_URL = os.getenv("DATABASE_URL")

#the main connection to the databse
engine=create_engine(DATABASE_URL)

#creates database sessions(like openning a connection)
SessionLocal= sessionmaker(autocommit =False, autoflush=False, bind=engine)

#a base class for our database mdels
Base = declarative_base()


class ExpenseDB(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True, index=True)
    description = Column(String, nullable = False)
    amount = Column(Float, nullable = False)

