from fastapi import APIRouter,Form,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..db import get_db
from ..model import User
from ..utils import verify_password
from ..schemas import UserOut
from ..utils import create_token
from ..dependecis import username_status,verify_user_exists
from ..services import db_create_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post("",response_model=UserOut)
async def register(
    password:str = Form(min_length=8),
    username:str = Depends(username_status),
    db:Session = Depends(get_db)
):
    return db_create_user(db,username,password)

@router.post('/login')
async def login(
    user: User = Depends(verify_user_exists),
    password:str = Form(min_length=8),
    db = Depends(get_db)
    ):

    if not verify_password(password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Password xato')
    
    token = create_token(user)
    
    return {
        'token':token
    }
