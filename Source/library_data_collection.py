import json
import math
from collections import Counter
from enum import Enum

DDC_dict = {
    0: "Computer Science, Information & General Works",
    100: "Philosophy & Psychology",
    200: "Religion",
    300: "Social Sciences",
    400: "Language",
    500: "Pure Science",
    600: "Applied Science",
    700: "Arts & Recreation",
    800: "Literature",
    900: "History & Geography"
}

RECORDS = {}

def load_data(file='../Records/test_data.json'):
    with open(file) as f:
        RECORDS = json.load(f)

    return RECORDS

def update_web_records(new_record, records_filepath):
    with open(records_filepath) as f:
        data = json.load(f)

    record_for_input = format_incoming_record(new_record)

    data['return_records'].append(record_for_input)

    with open(records_filepath, 'w') as f:
        json.dump(data,f,indent=4)

def format_incoming_record(new_record):
    new_record.pop('rating_selection')
    new_record.pop('time_to_read_selection')
    new_record.pop('town_resident')
    new_record.pop('Name')
    return new_record

def validate_ddc(ddc):
    valid = True
    if(len(ddc) < 3):
        valid = False

    try:
        ddc = int(ddc[0:3])
    except:
        valid = False

    return valid

def get_total_pages_read(RECORDS):
    pages_read = 0
    for record in RECORDS['return_records']:
        if record['Read'] == 'Fully':
            pages_read += int(record['Pages'])
        elif record['Read'] == 'Partially':
            pages_read += int(record['Pages'])/2

    return pages_read

def get_total_pages_per_ddc(RECORDS):
    ddc_list = []
    for record in RECORDS['return_records']:
        ddc_list.append(get_ddc_for_value(record['DDC']))
    ddc_names = get_DDC_names(ddc_list)
    ddc_count = Counter(ddc_names)
    ddc_json = json.dumps(ddc_count,indent=4)
    return ddc_json

def get_ddc_for_value(ddc):
    ddc = int(ddc[0:3]) #gets first 3 items in string
    ddc_floor = math.floor(ddc /100) * 100
    return ddc_floor #returns DDC Category number. Reference DDC_dict for values

def get_DDC_names(ddc_list):
    ddc_names = []
    for ddc_code in ddc_list:
        ddc_names.append(DDC_dict[ddc_code])
       # ddc_names.append(DDC_Names[(DDC(ddc_code).name)])
    return ddc_names

def get_Records():
    return RECORDS



