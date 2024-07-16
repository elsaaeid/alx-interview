#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def compute_metrics():
    """Function that reads stdin line
    by line and computes metrics.
    """
    # Initialize variables
    total_size = 0
    status_codes = {}

    try:
        # Read input from stdin line by line
        for line_number, line in enumerate(sys.stdin, start=1):
            # Split the line into its components
            parts = line.split()

            # Check if the line has the expected format
            if len(parts) != 7:
                continue

            # Extract the file size and status code
            file_size = int(parts[6])
            status_code = int(parts[5])

            # Update the total file size
            total_size += file_size

            # Update the count for the status code
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_codes.keys()):
                    print(f"{code}: {status_codes[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")

# Call the compute_metrics function
compute_metrics()
