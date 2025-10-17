from fastapi import FastAPI

from app.db import Base ,engine
from app.model import User,Task
from app.router.users import router as user_router
from app.router.tasks import router as task_router

Base.metadata.create_all(engine)

app = FastAPI(
    title='Todos api'
)

app.include_router(user_router)
app.include_router(task_router)