from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from . import models, schemas


app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./emp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"hello":"World"}

@app.post("/")
def createemp(fname:str,lname:str,emp_id:str,city:str,age:int,contactno:int,experience:int):
    return{fname,lname,emp_id,city,age,contactno,experience}


class User(Base):
    __tablename__ = "empdetails"

    emp_id = Column(Integer,unique=True, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    city = Column(String)
    age = Column(Integer)
    contanctno = Column(Integer)
    experienece = Column(Integer)

Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    first_name: str
    last_name:str
    employee_id: str
    city: str
    experience: float
    ctc:float
    age:float
    contact: str

class Config:
    orm_mode = True



def get_emp(db: Session, emp_id: int):
    return db.query(models.emp).filter(models.emp.id == emp_id).first()

def get_emp(db: Session, fname: str):
    return db.query(models.emp).filter(models.emp.fname == fname).first()

def get_emp(db: Session, lname: str):
    return db.query(models.emp).filter(models.emp.lname == lname).first()

def get_emp(db: Session, city: str):
    return db.query(models.emp).filter(models.emp.city == city).first()

def get_emp(db: Session, age: int):
    return db.query(models.emp).filter(models.emp.age == age).first()

def get_emp(db: Session,contactno: int):
    return db.query(models.emp).filter(models.emp.contactno == contactno).first()

def get_emp(db: Session, experience: int):
    return db.query(models.emp).filter(models.emp.experienece == experience).first()



def get_emp(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.emp).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(User).where(User.id == emp_id).first()

def get_items(db: Session):
    return db.query(User).all()

def create_item(db: Session, item: Item):
    db_item = User(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item