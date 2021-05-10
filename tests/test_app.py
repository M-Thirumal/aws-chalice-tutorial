from chalice.test import Client
from app import app
import pytest

#@pytest.mark.skip
def test_foo_function():
    with Client(app, stage_name='dev') as client:
        result = client.lambda_.invoke('foo')
        assert result.payload == {'value': 'TOP LEVEL'}


def test_pagination():
    with Client(app) as client:
        print("Started testing pagination")
        response = client.http.get('/pagination?page=0&limit=10')
        assert response.json_body == {'page':'0','limit':'10'}
