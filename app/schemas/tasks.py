from pydantic import BaseModel,Field
from typing import Annotated

class TaskCreate(BaseModel):
    title :Annotated[str,Field(max_length=128)]
    description:str|None = Field(None)
    status:bool
