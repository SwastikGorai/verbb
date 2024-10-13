from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class SchoolEmail(BaseModel):
    school_name: str
    teacher_name: str
    email: EmailStr
    is_active: bool
    
    
class VerifySchoolEmail(BaseModel):
    email: EmailStr
    