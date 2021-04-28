from chalice.test import Client
from app import app


def test_foo_function():
    with Client(app, stage_name='dev') as client:
        result = client.lambda_.invoke('foo')
        assert result.payload == {'value': 'TOP LEVEL'}