import requests
import pytest
import flask
from Source import library_web_api

url="http://127.0.0.1:5000"

def test_GET_badPath_Fail():
    response = requests.get(url + '/path-does-not-exist')
    assert response.status_code == 404