from sqlalchemy import Column,String,Integer
from ..db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(length=128),nullable=False,unique=True)
    hash_password = Column(String,nullable=False)

    def __repr__(self):
        return f"User(id = {self.id} username = {self.username} hash_password = {self.hash_password})"
    