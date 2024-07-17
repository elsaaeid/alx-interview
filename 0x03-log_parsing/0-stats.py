#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_statistics(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        splt_line = line.split()
        splt_line = splt_line[::-1]

        if len(splt_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(splt_line[0])
                code = splt_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_lines == 10):
                print_statistics(codes, file_size)
                count_lines = 0

finally:
    print_statistics(codes, file_size)
