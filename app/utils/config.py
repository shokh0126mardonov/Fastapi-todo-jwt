from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DB_PORT = os.getenv("DB_PORT")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")

config = Config()