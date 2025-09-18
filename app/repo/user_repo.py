from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db import User
from app.schemas.user_schemas import UserCreate


def add_user(db:Session,user_create_dto:UserCreate):
    db_user = User(**user_create_dto.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh()
    return db_user

def get_user_by_username(db:Session,username:str):
    return  db.query(User).filter_by(username=username).first()
