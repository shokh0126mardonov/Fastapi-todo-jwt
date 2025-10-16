from datetime import datetime,timedelta

import jwt

from .config import config

def create_token(user:str):
    payload = {
        'sub':user.id,
        'username':user.username,
        'exp':datetime.utcnow() + timedelta(minutes=15)
    }
    token = jwt.encode(payload,config.SECRET_KEY,'HS256')

    return token