import os

from sqlalchemy.engine.url import URL
from sqlmodel import Session, create_engine
from fastapi_templates.constant import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

# DB接続
url = URL.create(
    username=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    host=DB_HOST,
    drivername="mysql+pymysql",
)

engine = create_engine(url, echo=True)


async def get_session():
    with Session(engine) as session:
        yield session
