from datetime import datetime,timedelta

import jwt

from .config import config

def create_token(user): 
    payload = {
        "sub": str(user.id),           
        "username": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    # payload = {
    #     "sub": '3',           
    #     "username": "artur_settarov",
    #     "exp": datetime.utcnow() + timedelta(minutes=15)
    # }
    token = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token:str):
    # try:
        decoded_payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    # except jwt.ExpiredSignatureError:
    #     print("Token has expired!")
    # except jwt.InvalidTokenError:
    #     print("Invalid token!")