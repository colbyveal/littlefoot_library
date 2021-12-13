# LittleFoot Library Test Plan

## LittleFoot Summary

LittleFoot Library contains the following parts:

- `library_data_collection.py`: backend service for processing data
- `process_records.py`: middle layer interface for running `library_data_collection.py` and defining input. This is for local testing only.
- `library_web_api.py`: REST api that calls functions from `library_data_collection.py`
- `index.html`: UI layer for creating records for end-users via the web

## Test Strategy

- [Unit Testing](unit-testing)
- [API Testing](api-testing)
- [UI Testing](ui-testing)
- [End to End Testing](end-to-end-testing)

## Unit Testing

At the Unit Testing level, we should target each function within our backend service. This is to include
positive and negative test case and any edge cases. We should NOT be interacting via interfaces with
the underlying functions and is to be performed at the lowest level (in our case, `library_data_collection.py`)

Can be executed via `python -m pytest Source/QA/unit_test.py` from root

## API Testing

At the API Testing level, we will be excerising code through the `library_web_api.py` entry point. We should 
call each API and trigger both happy paths and exceptions for them and ensure our return values are what we
expect. We will need to create mock json data to trigger certain scenarios. 

Can be executed via `python -m pytest Source/QA/api_test.py` from root

## UI Testing

At the UI Level, we will be interacting with the webpage `library_input.html` and ensure the behavior is as expected. This includes things
like button clicks, test box entry, page loading. We will test functionality that is listed in the requirements - not additional pages we've created
development or testing purposes that will not make it to live production as this is wasted testing effort. If it is decided one of these test
views will make it to public, we will address testing at that time.

Can be executed via `python -m pytest Source/QA/ui_test.py` from root

# End to End Testing

Finally, a happy path e2e test should be created and fully automated. This will include interacting with the UI to submit a new record,
and then ensuring that the response is correct. Then, checking the server to ensure the record as added to the web_records.json.

Can be executed via `python -m pytest Source/QA/e2e_test.py` from root