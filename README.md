# LittleFoot Library

## Acceptance Criteria

littlefoot_library is a system that can analyze input, a JSON object containing records of reading log from
patrons of the library, and return a report of total pages read as well as total pages read per Dewie-decimal system catagory
The Dewie Decimal System is as follows:

- 000 – Computer Science, Information & General Works
- 100 – Philosophy & Psychology
- 200 – Religion
- 300 – Social Sciences
- 400 – Language
- 500 – Pure Science
- 600 – Applied Science
- 700 – Arts & Recreation
- 800 – Literature
- 900 – History & Geography

## Dependencies

- Python 3.9.2
- All other dependencies can be found in requirements.txt

In order to install dependencies, run `pip3 install -r requirements.txt`

## Start Up

littlefoot_library at current can be run via 2 methods:

1. Via executing the command `python process_records.py`. This will execute the library against the default data file `test_data.json`, or executing the command `python process_records.py <filename>`, where `<filename>` is a json file for input. This requires no server to be running and only exercises the underlying libray.

2. Via first starting up a server by running `pythom -m flask run`. This will begin a flask server running on `localhost:5000`. Navigate to `localhost:5000` in your
browser and you will see a webpage with a form. Records can be posted to the library in this way as well.

## Overview

LittleBear Library API is a RESTful API supporting:

- GET
- POST

PUT, DELETE were outside of the requirements and were not implemented

By default, the backend of this service is served by `web_records.json`. Unless specified otherwise, all posted records are recorded here.

### API
**Post Record**
POST /submit_action - Submits form data from webpage
POST /submit_action/<record>
```http
http://127.0.0.1:5000/submit_action/<record>
```
```
{
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
```
Response (Example):

Status Code:
```
200 - OK
```
Response body:
```
{
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
```
- Error Codes:
-- Pages is non-numeric || Pages is Empty
--- Status Code: 400
-- DDC is non-conforming to standard
--- Status Code: 400

**Get All Records**

GET /records

```http
http://127.0.0.1:5000/records
```

Response (Example):

Status Code:
```
200 - OK
```
Response body:
```json
{
    "return_records": [
        {
            "Title": "Presumptions of Philosophy",
            "Author": "Donald Daffy Duckworth",
            "Pages": "657",
            "DDC": "120.563DUC",
            "Read": "Fully"
        },
        {
            "Title": "Philosophical Ponderings",
            "Author": "Mickey and Minnie Mouse",
            "Pages": "1200",
            "DDC": "125.563MOU",
            "Read": "Partially"
        },
        {
            "Title": "Application of Natural Sciences",
            "Author": "Rick Sanchez",
            "Pages": "145",
            "DDC": "601.103SAN",
            "Read": "Fully"
        },
        {
            "Title": "Rented and Unread",
            "Author": "Solitude O'Brien",
            "Pages": "734",
            "DDC": "834.334OBR",
            "Read": "Unread"
        }
    ]
}
```

**Get Report**
```
http://127.0.0.1:5000/report
```
Response (Example):

Status Code:
```
200 - OK
```
Response body:
```json
'Total Pages Read : ': 1402, 
'By Category: ': 
    '{
        "Philosophy & Psychology": "1257", 
        "Applied Science": "145", 
        "Literature": "0"
    }'
```

## Testing

A detailed testplan exists in the `Source/QA` folder titled `README.md`. As an overview, this project contains:

- Unit Tests
- API Tests
- UI Tests
- End-to-End Test

In order to execute testing, the server must first be running. Ensure you've executed steps listed in [Start-Up](start-up) before attempting to run tests.
To execute the tests, run `python -m pytest` to run all tests, or `python -m pytest Source/QA/<testfile>` to run an individual test file.

## Output

littlefoot_library outputs a data report containing information on pages read by the libraries patrons. Here is an example report
using the `test_data.json` provided in the repo:

```
'Total Pages Read : ': 1402, 
'By Category: ': 
    '{
        "Philosophy & Psychology": "1257", 
        "Applied Science": "145", 
        "Literature": "0"
    }'
```

When running the server, visiting `localhost:5000/report` will run the report on all items within web_

## Github Actions

This project is set up to run a Github Action that triggers the running of Unit Tests in the Pipeline. Check the `Actions` tab for
status of runs.