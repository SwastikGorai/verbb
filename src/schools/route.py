from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import get_db
# from auth import get_current_user
from src.schemas import VerifySchoolEmail
from src.schools.models import SchoolEmail

router = APIRouter()


@router.post("/verify")
async def verify_email(email: VerifySchoolEmail, db: Session = Depends(get_db)):
    e = db.query(SchoolEmail).filter(SchoolEmail.email == email.email).first()
    if not e:
        raise HTTPException(status_code=404, detail="You're not registered")
    return e
