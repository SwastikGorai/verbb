from sqlalchemy import Column, String, Boolean, Integer
from src.db import Base

class SchoolEmail(Base):
    __tablename__ = "school_emails"

    school_name = Column(String, unique=True, index=True)
    teacher_name = Column(String)
    email = Column(String, unique=True, index=True, primary_key=True)
    is_active = Column(Boolean, default=True)
    
    
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String)
    school_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
