#!/usr/bin/python3
import sys

def print_statistics(total_size, status_code_counts):
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def main():
    lines_processed = 0
    total_size = 0
    status_code_counts = {}

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line)
            if ip_address is not None:
                lines_processed += 1
                total_size += file_size
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            if lines_processed % 10 == 0:
                print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_statistics(total_size, status_code_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
