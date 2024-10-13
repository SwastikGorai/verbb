from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
# from auth import get_current_user
from schemas import VerifySchoolEmail
from models import SchoolEmail

router = APIRouter()


@router.post("/verify")
async def verify_email(email: VerifySchoolEmail, db: Session = Depends(get_db)):
    e = db.query(SchoolEmail).filter(SchoolEmail.email == email.email).first()
    if not e:
        raise HTTPException(status_code=404, detail="You're not registered")
    return {"email": e.email, "is_active": e.is_active}
