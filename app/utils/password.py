from passlib.context import CryptContext

from app.utils import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password:str)->str:
    new_password = f"{password}:{config.SECRET_KEY}"
    return pwd_context.hash(new_password)

def verify_password(password,hash_password)->bool:
    new_password = f"{password}:{config.SECRET_KEY}"
    return pwd_context.verify(new_password,hash_password)