#!/usr/bin/python3
"""101-stats.py - Reads stdin line by line and computes metrics
"""
import sys


def print_metrics(total_size, status_codes):
    """Prints the metrics to stdout
    
    Arguments:
        total_size {int} -- Total size of the file
        status_codes {dict} -- Dictionary containing the status codes

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def process_line(line, total_size, status_codes):
    """Processes the line read from stdin

    Arguments:
        line {str} -- Line read from stdin
        total_size {int} -- Total size of the file
        status_codes {dict} -- Dictionary containing the status codes

    Returns:
        tuple -- Total size of the file and dictionary containing the status codes
    """
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = parts[-2]

        total_size += size

        if status_code in status_codes:
            status_codes[status_code] += 1

    except (ValueError, IndexError):
        pass

    return total_size, status_codes


def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0,
                    '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = process_line(line,
                                                    total_size,
                                                    status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
