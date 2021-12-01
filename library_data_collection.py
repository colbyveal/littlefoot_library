import json
import math
from collections import Counter
from enum import Enum


class DDC(Enum):
    CS_Info_General = 0
    Phil_Psych = 100
    Religion = 200
    Social = 300
    Language = 400
    Pure_Science = 500
    Applied_Science = 600
    Arts_Rec = 700
    Lit = 800
    History_Geo = 900

DDC_Names = {
    "CS_Info_General": "Computer Science, Information & General Works",
    "Phil_Psych": "Philosophy & Psychology",
    "Religion": "Religion",
    "Social":"Social Sciences",
    "Language":"Language",
    "Pure_Science":"Pure Science",
    "Applied_Science":"Applied Science",
    "Arts_Rec":"Arts & Recreation",
    "Lit":"Literature",
    "History_Geo":"History & Geography"
}

def load_data(file='test_data.json'):
    with open(file) as f:
        RECORDS = json.load(f)

    return RECORDS


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
    ddc = int(ddc[:-7])
    ddc_floor = math.floor(ddc /100) * 100
    return ddc_floor #returns DDC Category number. Reference DDC(Enum) for values

def get_DDC_names(ddc_list):
    ddc_names = []
    for ddc_code in ddc_list:
        ddc_names.append(DDC_Names[(DDC(ddc_code).name)])
    return ddc_names



