from sqlalchemy.orm import Session

from ..model import User
from ..utils import hashed_password


def db_create_user(
        db:Session,
        username:str,
        password:str
    ):
    user = User(
            username = username,
            hash_password = hashed_password(password)
        )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user