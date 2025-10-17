from fastapi import APIRouter,Depends
from typing import Annotated
from sqlalchemy.orm import Session

from .users import oauth2_scheme
from ..schemas import TaskCreate
from ..db import get_db

router = APIRouter(
    prefix='/tasks',
    tags=['Task Crud']
)

@router.get('')
async def get_task(
    task:TaskCreate,
    token:Annotated[str,Depends(oauth2_scheme)],
    db:Session = Depends(get_db)
    ):
    pass