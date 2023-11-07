#!/usr/bin/python3
"""
Module of a total_size class
"""
import sys

total_size = 0
status_codes = {
        '200': 0, '301': 0, '400': 0,
        '401': 0, '403': 0, '404': 0,
        '405': 0, '500': 0
        }

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            tokens = line.split()
            if len(tokens) >= 7:
                status = tokens[-2]
                size = int(tokens[-1])
                total_size += size
                if status in status_codes:
                    status_codes[status] += 1

            if i % 10 == 0:
                print("File size: {}".format(total_size))
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))

        except ValueError:
            pass

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
