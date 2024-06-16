from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Use a separate database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Override the get_db dependency to use the testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_leader():
    response = client.post(
        "/leaders/",
        json={"name": "Captain James Cutter", "faction": "UNSC", "background": "Experienced leader"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Captain James Cutter"
    assert response.json()["faction"] == "UNSC"

def test_read_leader():
    response = client.get("/leaders/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Captain James Cutter"