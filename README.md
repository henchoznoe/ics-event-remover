# ICS Event Remover

This Python script allows you to interactively remove multiple events from an ICS calendar file based on the event's `SUMMARY`. You specify the ICS file path via the command line, the script lists all event summaries, and you select which events to remove. The script then generates a modified version with the specified events removed, without altering the original file.

## Features

- Remove events based on their `SUMMARY` field.
- Interactive selection of events to remove.
- Processes and modifies `.ics` calendar files.
- The original file is not modified; the new file is prefixed with `edited_`.
- Supports removing multiple events in one execution.

## Requirements

This script requires Python 3.x to run.

No external dependencies are needed.

## Usage

1. Clone this repository.
2. Run the script from the command line, specifying the ICS file to process:

   ```bash
   python event_remover.py chemin/vers/ton_fichier.ics
   ```

3. The script will list all event summaries found in the file and prompt you to enter the numbers of the summaries to remove (comma separated).
4. The script will generate a new `.ics` file with the specified events removed. The new file will be named `edited_<nomoriginal>.ics` and saved in the same directory as the original.
