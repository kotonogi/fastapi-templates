import pytest
from factory.alchemy import SQLAlchemyModelFactory
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel
from fastapi_templates.db import engine, get_session
from fastapi_templates.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def create_table():
    SQLModel.metadata.create_all(engine)


@pytest.fixture(scope="session")
def db_session():
    """DBのセッションを作成し、すべて同じセッションを使用するように設定を行う"""
    from . import factories

    session = Session(engine)

    # fastapiのDependsのセッション取得をオーバーライド
    def session_override():
        yield session

    app.dependency_overrides[get_session] = session_override

    # すべてのファクトリーにおなじセッションを使用させる
    for factory in SQLAlchemyModelFactory.__subclasses__():
        factory._meta.sqlalchemy_session = session

    yield session

    session.close()


@pytest.fixture(scope="function")
def rollback(db_session):
    """関数間でDBのdataを共有しないように関数ごとにテーブルのデータを初期化する"""
    db_session.rollback()
