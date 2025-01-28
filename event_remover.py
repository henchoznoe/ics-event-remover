input_file = "myfile.ics"
output_file = "myfile_edited.ics"
summaries_to_remove = [
    "SUMMARY1...",
    "SUMMARY2..."
]

# Read the ICS file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

filtered_lines = []
inside_event = False
remove_event = False
event_buffer = []  # Temporary buffer to store event lines
removed_events_count = 0  # Counter for removed events

# Iterate through the lines of the file
for line in lines:
    if line.startswith("BEGIN:VEVENT"):
        inside_event = True
        remove_event = False  # Reset the flag for each new event
        event_buffer = []  # Initialize a new buffer for the current event
    if inside_event:
        event_buffer.append(line)
        if line.startswith("SUMMARY:") and any(summary in line for summary in summaries_to_remove):
            remove_event = True
    if line.startswith("END:VEVENT"):
        if remove_event:
            removed_events_count += 1  # Increment the counter for removed events
        else:
            filtered_lines.extend(event_buffer)  # Keep the event if not marked for removal
        inside_event = False  # Exit the event block
        event_buffer = []  # Clear the buffer
    elif not inside_event:
        # Add non-event lines directly to the filtered output
        filtered_lines.append(line)

# Write the filtered lines to the output ICS file
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)

# Print the result
print(f"Total events removed: {removed_events_count}")
print(f"Modified file saved as: {output_file}")