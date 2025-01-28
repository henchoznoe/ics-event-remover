# ICS Event Remover

This Python script allows you to remove multiple events from an ICS calendar file based on the event's `SUMMARY`. You can specify which events to remove by providing a list of summaries. The script will then process the ICS file and generate a modified version with the specified events removed.

## Features

- Remove events based on their `SUMMARY` field.
- Process and modify `.ics` calendar files.
- Supports removing multiple events in one execution.

## Requirements

This script requires Python 3.x to run.

No external dependencies are needed.

## Usage

1. Clone this repository
2. Modify the script to specify the ICS file you want to process and the event summaries to remove.
3. Run the script:

```bash
python event_remover.py
```

4. The script will generate a new .ics file with the specified events removed.
