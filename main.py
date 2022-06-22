from typing import Union
from app import models
from app.db import engine

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app= FastAPI()

@app.get("/")
def read_root():
    return {"hello":"World"}

@app.post("/")
def createemp(fname:str,lname:str,empid:str,city:str,age:int,contactno:int,experience:int):
    return{fname,lname,empid,city,age,contactno,experience}

SQLALCHEMY_DATABASE_URL = "sqlite:///./emp.db"

# create new engine instance 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create sessionmaker 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

models.Base.metadata.create_all(bind=engine)