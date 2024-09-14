from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import pytest
from main import app  
from sqlalchemy.orm import Session
from models import Car

client = TestClient(app)

@pytest.fixture
def mock_db_session():
    with patch('app.get_db') as mock:
        yield mock

def test_create_car(mock_db_session):
    mock_session = MagicMock()
    mock_db_session.return_value = mock_session
    mock_session.add = MagicMock()
    mock_session.commit = MagicMock()

    response = client.post("/cars/", json={"make": "Toyota", "model": "Corolla", "year": 2024})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "make": "Toyota", "model": "Corolla", "year": 2024}
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()

def test_retrieve_all_cars(mock_db_session):
    mock_session = MagicMock()
    mock_db_session.return_value = mock_session
    mock_session.query.return_value.all.return_value = [
        Car(id=1, make="Toyota", model="Corolla", year=2024),
        Car(id=2, make="Honda", model="Civic", year=2023)
    ]
    
    response = client.get("/cars/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]['make'] == "Toyota"

def test_retrieve_specific_car(mock_db_session):
    mock_session = MagicMock()
    mock_db_session.return_value = mock_session
    mock_session.query.return_value.filter_by.return_value.first.return_value = Car(id=1, make="Toyota", model="Corolla", year=2024)
    
    response = client.get("/cars/1")
    assert response.status_code == 200
    assert response.json()['make'] == "Toyota"

def test_update_car(mock_db_session):
    mock_session = MagicMock()
    mock_db_session.return_value = mock_session
    mock_session.query.return_value.filter_by.return_value.first.return_value = Car(id=1, make="Toyota", model="Corolla", year=2024)
    mock_session.commit = MagicMock()

    response = client.put("/cars/1", json={"make": "Toyota", "model": "Camry", "year": 2025})
    assert response.status_code == 200
    assert response.json()['model'] == "Camry"
    mock_session.commit.assert_called_once()

def test_delete_car(mock_db_session):
    mock_session = MagicMock()
    mock_db_session.return_value = mock_session
    mock_session.query.return_value.filter_by.return_value.first.return_value = Car(id=1, make="Toyota", model="Corolla", year=2024)
    mock_session.delete = MagicMock()
    mock_session.commit = MagicMock()

    response = client.delete("/cars/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Car deleted"}
    mock_session.delete.assert_called_once()
    mock_session.commit.assert_called_once()