import pytest
from Lambda_function_rqg_aws import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert 'headers' in response
    assert response['headers']['Content-Type'] == 'text/html'
    assert 'body' in response
