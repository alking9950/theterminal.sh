#!/usr/bin/env python
from __future__ import print_function
import os
import os.path
import sys


def bin_file_paths(path):
    file_paths = []
    for filename in os.listdir(path):
        if filename.endswith('.bin'):
            file_paths.append(os.path.join(path, filename))
    return file_paths


def hex_string_to_bytes(hex_string):
    from codecs import decode
    return decode(b''.join(hex_string.split()), 'hex')


def hex_string_to_integers(hex_string):
    return [int(x, 16) for x in hex_string.split()]


def int_to_ascii(number):
    from struct import pack
    try:
        return pack('>I', number).decode('ascii')
    except UnicodeDecodeError:
        return None


def output(values):
    for position in range(0, len(values), 4):
        print(' '.join(['{:10d}'.format(x)
                        for x in values[position:position + 4]]))


def read_file(path):
    with open(path, 'rb') as fp:
        return fp.read()


def write_file(path, data):
    with open(path, 'wb') as fp:
        fp.write(data)


def main():
    integers = []
    for path in bin_file_paths('./server_files'):
        binary_name = os.path.basename(path)
        integers.extend(hex_string_to_integers(read_file(path)))

    unique = set(integers)
    printable = set()
    for first in unique:
        for second in unique:
            result = int_to_ascii(first ^ second)
            if result:
                printable.add(result)

    for item in sorted(printable):
        print(item)
    return 0


if __name__ == '__main__':
    sys.exit(main())
