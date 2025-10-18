from fastapi import APIRouter,Form,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..db import get_db
from ..model import User
from ..utils import verify_password
from ..schemas import UserOut
from ..utils import create_token
from ..services import db_create_user
from ..dependecis import username_status

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post("",response_model=UserOut)
async def register(
    username:str = Depends(username_status),
    password:str = Form(min_length=8),
    db:Session = Depends(get_db)
):
    return db_create_user(db,username,password)

@router.post('/login')
async def login(
    username: str = Form(min_length=3, max_length=128),
    password: str = Form(min_length=8),
    db:Session = Depends(get_db)
    ):

    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bu foydalanuvchi mavjud emas"
        )
    if not verify_password(password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password.")
    
    token = create_token(user)
    
    return {
        'token':token
    }
