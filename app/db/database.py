from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

from ..utils import config

url = URL.create(
    'postgresql+psycopg2',
    config.DB_USER,
    config.DB_PASS,
    config.DB_HOST,
    config.DB_PORT,
    config.DB_NAME
)

engine = create_engine(url)
Base = declarative_base()
LocalSession = sessionmaker(bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()