# tests/test_app.py
#trying a change
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data
