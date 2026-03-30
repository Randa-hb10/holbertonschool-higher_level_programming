#!/usr/bin/python3
import sys


def generate_invitations(template, attendees):
    """Generate invitation files from a template and list of attendees."""

    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}", file=sys.stderr)
        return

    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, got {type(attendees).__name__}", file=sys.stderr)
        return

    if not all(isinstance(a, dict) for a in attendees):
        print("Error: All items in attendees list must be dictionaries", file=sys.stderr)
        return

    if not template.strip():
        print("Template is empty, no output files generated.", file=sys.stderr)
        return

    if not attendees:
        print("No data provided, no output files generated.", file=sys.stderr)
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        content = template

        for field in placeholders:
            value = attendee.get(field)
            if value is None:
                value = "N/A"

            content = content.replace(f"{{{field}}}", str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}", file=sys.stderr)
