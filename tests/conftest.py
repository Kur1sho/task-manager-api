import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app, get_db
from app.database import Base

# In-memory SQLite for tests (fast + isolated)
TEST_DATABASE_URL = "sqlite+pysqlite://"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # keeps the same in-memory DB across connections
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables once per test session
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture()
def client():
    return TestClient(app)
