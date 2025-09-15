# tests/test_app.py
#trying a change 2
# NEW_FEATURE BRANCH CHANGE
# NEW_FEATURE 23
#STATUS
#COMMIT1
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data
