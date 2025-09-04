import argparse
import os

def get_summaries(file_path):
    summaries = set()
    with open(file_path, "r", encoding="utf-8") as file:
        inside_event = False
        for line in file:
            if line.startswith("BEGIN:VEVENT"):
                inside_event = True
            if inside_event and line.startswith("SUMMARY:"):
                summary = line[len("SUMMARY:"):].strip()
                summaries.add(summary)
            if line.startswith("END:VEVENT"):
                inside_event = False
    return list(summaries)

def main():
    parser = argparse.ArgumentParser(description="Remove events from ICS file by SUMMARY.")
    parser.add_argument("ics_path", help="Path to the ICS file")
    args = parser.parse_args()

    input_file = args.ics_path
    base_name = os.path.basename(input_file)
    output_file = os.path.join(os.path.dirname(input_file), f"edited_{base_name}")

    # Step 1: List all summaries
    summaries = get_summaries(input_file)
    if not summaries:
        print("No event summaries found in the file.")
        return
    print("Event summaries found:")
    for idx, summary in enumerate(summaries, 1):
        print(f"{idx}. {summary}")

    # Step 2: Ask user which summaries to remove
    to_remove = input("Enter the numbers of the summaries to remove (comma separated): ")
    try:
        indices = [int(x.strip()) for x in to_remove.split(",") if x.strip()]
        summaries_to_remove = [summaries[i-1] for i in indices if 1 <= i <= len(summaries)]
    except Exception as e:
        print("Invalid input.")
        return
    if not summaries_to_remove:
        print("No valid summaries selected for removal.")
        return

    # Step 3: Process the file
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    filtered_lines = []
    inside_event = False
    remove_event = False
    event_buffer = []
    removed_events_count = 0

    for line in lines:
        if line.startswith("BEGIN:VEVENT"):
            inside_event = True
            remove_event = False
            event_buffer = []
        if inside_event:
            event_buffer.append(line)
            if line.startswith("SUMMARY:") and any(summary == line[len("SUMMARY:"):].strip() for summary in summaries_to_remove):
                remove_event = True
        if line.startswith("END:VEVENT"):
            if remove_event:
                removed_events_count += 1
            else:
                filtered_lines.extend(event_buffer)
            inside_event = False
            event_buffer = []
        elif not inside_event:
            filtered_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(filtered_lines)

    print(f"Total events removed: {removed_events_count}")
    print(f"Modified file saved as: {output_file}")

if __name__ == "__main__":
    main()
