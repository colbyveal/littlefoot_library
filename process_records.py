from library_data_collection import *
import sys

if (len(sys.argv) > 1):
    records = load_data(sys.argv[1])
else:
    records = load_data()
print(json.dumps(records, indent=4))

pages = get_total_pages_read(records)
print('Total Pages Read: ', int(pages))

ddc = get_total_pages_per_ddc(records)
print ('By Catagory: ', ddc)
