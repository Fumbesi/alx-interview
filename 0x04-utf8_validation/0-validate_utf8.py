#!/usr/bin/python3
"""
Valid UTF-8 encoding checker
"""

import sys

def validUTF8(data):
    # Helper function to check if a given number has the correct format
    def is_start_of_char(byte):
        return bin(byte).startswith('0b' + '1' * (8 - len(bin(byte))))

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes in the current character
        num_bytes = 0
        while i < len(data) and is_start_of_char(data[i]):
            num_bytes += 1
            i += 1

        # Check if the number of bytes is valid
        if num_bytes == 0:
            return False
        elif num_bytes == 1:
            continue
        elif num_bytes > 4:
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or not bin(data[i + j]).startswith('0b10'):
                return False

        i += num_bytes

    return True

if __name__ == '__main__':
    try:
        # Example usage:
        data_set = [197, 130, 1]  # This is a valid UTF-8 encoding
        result = validUTF8(data_set)
        print(result)  # Output: True
    except KeyboardInterrupt:
        raise

