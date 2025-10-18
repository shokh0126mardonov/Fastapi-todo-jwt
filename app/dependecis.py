from fastapi import HTTPException, status, Depends, Form
from sqlalchemy.orm import Session
from typing import Annotated

from .model import User
from .db import get_db

def username_status(
    username: str = Form(min_length=3, max_length=128),
    db:Session =  Depends(get_db)
):
    existing_user = db.query(User).filter_by(username=username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bu foydalanuvchi allaqachon yaratilgan'
        )

    return username

