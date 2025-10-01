import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import get_db, Base
from app.models import User, Task

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(setup_database):
    with TestClient(app) as test_client:
        yield test_client

def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Task Management API" in response.json()["message"]

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_user_registration(client):
    """Test user registration"""
    user_data = {
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]

def test_user_login(client):
    """Test user login"""
    # First register a user
    user_data = {
        "email": "login@example.com",
        "full_name": "Login User",
        "password": "testpassword123"
    }
    client.post("/register", json=user_data)
    
    # Then login
    login_data = {
        "username": "login@example.com",
        "password": "testpassword123"
    }
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task(client):
    """Test task creation"""
    # Register and login user
    user_data = {
        "email": "task@example.com", 
        "full_name": "Task User",
        "password": "testpassword123"
    }
    client.post("/register", json=user_data)
    
    login_response = client.post("/token", data={
        "username": "task@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]
    
    # Create task
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "priority": "high"
    }
    response = client.post(
        "/tasks",
        json=task_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == task_data["title"]