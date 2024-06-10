from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Boolean, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)
    created_at = Column(DATETIME, nullable=True)


class Bodypart(Base):
    __tablename__ = 'bodypart'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class UserBodypart(Base):
    __tablename__ = 'user_bodypart'

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    bodypart_id = Column(Integer, ForeignKey("bodypart.id"), primary_key=True)
    last_exercise = Column(DATETIME, nullable=True)
    primary_or_secondary = Column(String, nullable=True)

    user = relationship("User", back_populates="user_bodypart")
    bodypart = relationship("Bodypart", back_populates="user_bodypart")

    __table_args__ = (PrimaryKeyConstraint("user_id", "bodypart_id"),)


# Backref relationships
User.user_bodypart = relationship("UserBodypart", back_populates="user")
Bodypart.user_bodypart = relationship("UserBodypart", back_populates="bodypart")
