from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)
    created_at = Column(DATETIME, nullable=False)


class Bodypart(Base):
    __tablename__ = 'bodypart'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
