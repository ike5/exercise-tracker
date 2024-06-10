from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

import models
from models import User, Bodypart, UserBodypart
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# pydantic
class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=20)


@app.post("/user/")
def create_user(user_data: UserCreate, db: db_dependency):
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/users")
def read_users(db: db_dependency):
    user_model = db.query(User).all()
    return user_model
