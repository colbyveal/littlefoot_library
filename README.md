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

## Usage

littlefoot_library at current can be run via 2 methods:

1. Via executing the command `python process_records.py`. This will execute the library against the default data file `test_data.json`
2. Via executing the command `python process_records.py <filename>`, where `<filename>` is a json file for input

## Testing

A detailed testplan exists in the `QA` folder titled `Testplan.md`

## Output

littlefoot_library outputs a data report containing information on pages read by the libraries patrons. Here is an example report
using the `test_data.json` provided in the repo:

```
Total Pages Read: 1402
By Catagory: {
	"Philosophy & Psychology": 2,
	"Applied Science": 1,
	"Literature": 1
}
```