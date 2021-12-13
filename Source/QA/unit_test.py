import pytest
import json
from Source import library_data_collection

RECORDS = {
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

RECORD = {
            "Title": "Test Title",
            "Author": "Test Author",
            "Pages": "734",
            "DDC": "834.334OBR",
            "Read": "Unread"
        }

RECORD_WEB = {
            "Title": "Test Title",
            "Author": "Test Author",
            "Pages": "734",
            "DDC": "834.334OBR",
            "Read": "Unread",
            'rating_selection': '5',
            'time_to_read_selection': '1 week',
            'town_resident': 'Yes',
            'Name': 'Test User'
        }

REPORT = {'Total Pages Read : ': 1402, 'Books Per Category: ': '{"Philosophy & Psychology": "1857", "Applied Science": "145", "Literature": "734"}'}

testdata_filepath = './Records/test_data.json'
qadata_filepath = './Records/QA_data.json'

#get_total_pages_per_ddc Tests
def test_get_total_pages_per_ddc_SUCCESS():
    pages_per_ddc = library_data_collection.get_total_pages_per_ddc(RECORDS)
    assert pages_per_ddc == '{"Philosophy & Psychology": "1857", "Applied Science": "145", "Literature": "734"}'

#get_ddc_for_valueTests
def test_get_ddc_for_value_SUCCESS():
    ddc = library_data_collection.get_ddc_for_value('834.334OBR')
    assert ddc == 800

# get_DDC_names Tests
def test_get_DDC_names_SUCCESS():
    ddc_list = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    expected_result = ["Computer Science, Information & General Works","Philosophy & Psychology","Religion","Social Sciences","Language","Pure Science","Applied Science","Arts & Recreation", "Literature","History & Geography"]
    ddc_name = library_data_collection.get_DDC_names(ddc_list)
    assert ddc_name == expected_result

#process_report Tests
def test_process_report_SUCCESS():
    report = library_data_collection.process_report(RECORDS)
    assert report == REPORT

#loadData Tests
def test_loadData_passNoFilePath_SUCCESS():
    result = library_data_collection.load_data()
    assert result == RECORDS

def test_loadData_passFilePath_SUCCESS():
    result = library_data_collection.load_data(testdata_filepath)
    assert result == RECORDS

#update_web_records Tests
def test_update_web_records_SUCCESS():
    testlist = RECORDS.copy()
    test_weblist = RECORD_WEB.copy()
    library_data_collection.update_web_records(test_weblist, qadata_filepath)
    result = library_data_collection.load_data(qadata_filepath)
    reset_QA_data()
    testlist['return_records'].append(RECORD)
    assert result == testlist

#format_record Tests
def test_format_incoming_web_record_SUCCESS():
    test_weblist = RECORD_WEB.copy()
    formatted_record = library_data_collection.format_incoming_record(test_weblist)
    assert formatted_record == RECORD

#validate_ddc Tests
def test_validate_ddc_valid_SUCCESS():
    ddc = '834.334OBR'
    result = library_data_collection.validate_ddc(ddc)
    assert result

def test_validate_ddc_invalid_tooShort_NEGATIVE():
    ddc = '83'
    result = library_data_collection.validate_ddc(ddc)
    assert not result 

def test_validate_ddc_invalid_incorrectFormat_NEGATIVE():
    ddc = 'abc83'
    result = library_data_collection.validate_ddc(ddc)
    assert not result

def test_validate_ddc_invalid_empty_NEGATIVE():
    ddc = ''
    result = library_data_collection.validate_ddc(ddc)
    assert not result

#get_total_pages_read Tests
def test_get_total_pages_read_SUCCESS():
    pages_read =  library_data_collection.get_total_pages_read(RECORDS)
    assert pages_read == 1402

#----------------------------------------------------------
#Helper Functions
def reset_QA_data():
    with open(qadata_filepath, 'w') as f:
        json.dump(RECORDS,f,indent=4)



    