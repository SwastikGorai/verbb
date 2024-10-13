from sqlalchemy import Column, String
from src.db import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, primary_key=True)
    hashed_password = Column(String)
