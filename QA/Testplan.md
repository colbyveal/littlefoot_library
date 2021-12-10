# LittleFoot Library Test Plan

## LittleFoot Summary

LittleFoot Library contains the following parts:

- `library_data_collection.py`: backend service for processing data
- `process_records.py`: middle layer interface for running `library_data_collection.py` and defining input
- `library_input.html`: UI layer for creating records for end-users via the web

## Test Strategy

- [Unit Testing](unit-testing)
- [Integration Testing](integration-testing)
- [UI Testing](ui-testing) (Not implemented as part of this project)

## Unit Testing

At the Unit Testing level, we should target each function within our backend service. This is to include
positive and negative test case and any edge cases. We should NOT be interacting via interfaces with
the underlying functions and is to be performed at the lowest level (in our case, `library_data_collection.py`)

## Integration Testing

At the Integration Test level, we will interact with the system through the `process_records.py` layer.
This should involve creating various test data scenarios, with json files named in the fashion of `<testNumber_testName.json>`
with those corresponding to the testNumber and testName of the Integration test that uses it. At this level, no calls
are to be made directly to our server side code (in our case, `library_data_collection.py`). 

NOT being tested are scenarios in which are not possible via our UI Interface (empty text boxes, etc)

## UI Testing

At the UI Level, we will be interacting with the webpage `library_input.html` and ensure the behavior is as expected. This includes things
like button clicks, test box entry (and the rules around those text boxes), 