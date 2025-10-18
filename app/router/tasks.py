from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlalchemy.orm import Session

from ..schemas import TaskCreate
from ..db import get_db
from ..utils import decode_token

router = APIRouter(
    prefix='/tasks',
    tags=['Task Crud']
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

@router.post('')
async def get_task(
    task:TaskCreate,
    token:Annotated[str,Depends(oauth2_scheme)],
    db:Session = Depends(get_db)
    ):
    data = decode_token(token)
    
    return {
        'data':data
    }