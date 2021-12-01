import json
import math
from collections import Counter
from enum import Enum

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
    #ddc_json = json.dumps(ddc_list)
    ddc_count = Counter(ddc_list)
    return ddc_count

def get_ddc_for_value(ddc):
    ddc = int(ddc[:-7])
    ddc_floor = math.floor(ddc /100) * 100
    return ddc_floor #returns DDC Category number. Reference DDC(Enum) for values

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
