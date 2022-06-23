from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user(db: Session, fname: str):
    return db.query(models.User).filter(models.User.fname == fname).first()

def get_user(db: Session, lname: str):
    return db.query(models.User).filter(models.User.lname == lname).first()

def get_user(db: Session, city: str):
    return db.query(models.User).filter(models.User.city == city).first()

def get_user(db: Session, age: int):
    return db.query(models.User).filter(models.User.age == age).first()

def get_user(db: Session,contactno: int):
    return db.query(models.User).filter(models.User.contactno == contactno).first()

def get_user(db: Session, experience: int):
    return db.query(models.User).filter(models.User.experienece == experience).first()



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp
