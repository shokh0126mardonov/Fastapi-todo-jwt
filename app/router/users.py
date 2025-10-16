from fastapi import APIRouter,Form,Depends,HTTPException,status
from sqlalchemy.orm import Session

from ..db import LocalSession,get_db
from ..model import User
from ..utils import hashed_password,verify_password
from ..schemas import UserOut


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post("",response_model=UserOut)
async def register(
    username:str = Form(min_length=3,max_length=128),
    password:str = Form(min_length=8),
    db:Session = Depends(get_db)
):
    existing_user = db.query(User).filter_by(username = username).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='bu user yaratilgan')
    
    user = User(
        username = username,
        hash_password = hashed_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

@router.post('')
async def login(
    username:str,
    password:str,
    db:Session = Depends(get_db)
    ):
    
    user = db.query(User).filter_by(username = username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Bu user mavjud emas')
    existing_pass = verify_password(password,user.hash_password)
    return existing_pass