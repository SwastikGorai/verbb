from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import create_access_token, get_current_user, verify_password, get_password_hash
from schemas import Token, UserCreate
from models import User
from schools.models import SchoolEmail
from db import get_db
router = APIRouter()


def get_user(db, email: str):
    return db.query(User).filter(User.email == email).first()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    return {"email": new_user.email, "message": "User created successfully"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/add_school")
async def add_school_email(email_update: SchoolEmail, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    e = db.query(SchoolEmail).filter(SchoolEmail.email == email_update.email).first()
    if e:
        raise HTTPException(status_code=400, detail="Email already registered")
    new = SchoolEmail(email=email_update.email, is_active=email_update.is_active)
    db.add(new)
    db.commit()
    db.refresh(new)
    return {"email": new.email, "is_active": new.is_active}

@router.put("/update_school")
async def update_school_email(email_update: SchoolEmail, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    model = db.query(SchoolEmail).filter(SchoolEmail.email == email_update.email).first()
    if not model:
        raise HTTPException(status_code=404, detail="Email not found")
    update_data = email_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(model, key, value)
    db.commit()
    db.refresh(model)
    return {"email": model.email, "is_active": model.is_active}


@router.post("/remove_email")
async def remove_school_email(email_update: SchoolEmail, current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    model = db.query(SchoolEmail).filter(SchoolEmail.email == email_update.email).first()
    if not model:
        raise HTTPException(status_code=404, detail="Email not found")
    db.delete(model)
    db.commit()
    return {"email": model.email, "is_active": model.is_active, "message": "Email removed successfully"}

@router.get("/get_schools")
async def get_schools(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    schools = db.query(SchoolEmail).all()
    if not schools:
        raise HTTPException(status_code=404, detail="No schools found")
    return schools