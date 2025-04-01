import pytest
from app import app

def test_show_time():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode().count(',') == 2

