from library_data_collection import *
import sys

if (len(sys.argv) > 1):
    records = load_data(sys.argv[1])
else:
    records = load_data()
print(json.dumps(records, indent=4))

print(process_report(records))
