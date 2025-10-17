from sqlalchemy import Column,String,ForeignKey,Integer,Text,Boolean

from ..db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(128),nullable=False)
    description = Column(Text,default='')
    status = Column(Boolean,nullable=False,default=False)
    user_id = Column(ForeignKey('users.id'),nullable=False)

    def __repr__(self):
        return f"Task(id = {self.id}, title = {self.title}, description = {self.description})"