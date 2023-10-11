import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_ping_route(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'pong', 'api': 'flask'}

def test_pong_route(client):
    response = client.get('/pong')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'ping', 'api': 'flask'}
