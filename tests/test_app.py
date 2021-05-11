from chalice.test import Client
from app import app
import pytest


#Testing AWS Lambda functions
# client.lambda_ – Used to test Lambda functions by specifying the payload to pass to the Lambda function.
#@pytest.mark.skip
def test_foo_function():
    with Client(app, stage_name='dev') as client:
        result = client.lambda_.invoke('foo')
        assert result.payload == {'value': 'TOP LEVEL'}

# Testing REST API
# client.http – Used to test REST APIs.
def test_pagination():
    with Client(app) as client:
        print("Started testing pagination")
        response = client.http.get('/pagination?page=0&limit=10')
        assert response.json_body == {'page':'0','limit':'10'}
