import requests
import pytest
import flask
import json
from Source import library_web_api
from Source import library_data_collection

url="http://127.0.0.1:5000"
WEB_RECORDS = {}

def pytest_sessionstart(session):
    WEB_RECORDS = library_data_collection.load_data('Records/web_records.json')

def test_GET_badPath_Fail():
    response = requests.get(url + '/path-does-not-exist')
    assert response.status_code == 404

def test_GET_index_SUCCESS():
    response = requests.get(url + '/')
    assert response.status_code == 200

def test_GET_records_SUCCESS():
    response = requests.get(url + '/records')
    assert response.status_code == 200
    web_records = library_data_collection.load_data('Records/web_records.json')
    assert json.loads(response.content) == web_records

def test_POST_submit_SUCCESS():
    web_record = {
        "Title": "Test Title",
        "Author": "Test Author",
        "Pages": "734",
        "DDC": "834.334OBR",
        "Read": "Unread",
        "rating_selection": "5",
        "time_to_read_selection": "1 week",
        "town_resident": "Yes",
        "Name": "Test User"
    }
    html_response = "<html>\n    <body>\n        <p id=result>{&#39;Title&#39;: &#39;Test Title&#39;, &#39;Author&#39;: &#39;Test Author&#39;, &#39;Pages&#39;: &#39;734&#39;, &#39;DDC&#39;: &#39;834.334OBR&#39;, &#39;Read&#39;: &#39;Unread&#39;}</p>\n    </body>\n</html>"
    response = requests.post(url + '/submit_action/' + json.dumps(web_record))
    print(response.text)
    assert response.status_code == 200
    assert response.text == html_response

def test_POST_submit_noPageNum_NEGATIVE():
        web_record = {
            "Title": "Test Title",
            "Author": "Test Author",
            "Pages": "",
            "DDC": "834.334OBR",
            "Read": "Unread",
            "rating_selection": "5",
            "time_to_read_selection": "1 week",
            "town_resident": "Yes",
            "Name": "Test User"
        }
        response = requests.post(url + '/submit_action/' + json.dumps(web_record))
        assert response.status_code == 400
        assert response.text == '"400: Please include Number of Pages when submitting"\n'

def test_POST_submit_invalidDDCFormat_NotLongEnough_NEGATIVE():
        web_record = {
            "Title": "Test Title",
            "Author": "Test Author",
            "Pages": "123",
            "DDC": "8",
            "Read": "Unread",
            "rating_selection": "5",
            "time_to_read_selection": "1 week",
            "town_resident": "Yes",
            "Name": "Test User"
        }
        response = requests.post(url + '/submit_action/' + json.dumps(web_record))
        assert response.status_code == 400
        assert response.text == '"400: DDC not valid"\n'

def test_POST_submit_invalidDDCFormat_FirstThreeCharNotInt_NEGATIVE():
        web_record = {
            "Title": "Test Title",
            "Author": "Test Author",
            "Pages": "123",
            "DDC": "ab23423",
            "Read": "Unread",
            "rating_selection": "5",
            "time_to_read_selection": "1 week",
            "town_resident": "Yes",
            "Name": "Test User"
        }
        response = requests.post(url + '/submit_action/' + json.dumps(web_record))
        assert response.status_code == 400
        assert response.text == '"400: DDC not valid"\n'

def pytest_sessionfinish(session, exitstatus):
    with open('Records/web_records.json', 'w') as f:
        json.dump(WEB_RECORDS,f,indent=4)