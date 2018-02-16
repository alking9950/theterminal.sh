#!/usr/bin/env python
from __future__ import print_function
import os
import os.path
import sys

from codecs import decode


def bin_file_paths(path):
    file_paths = []
    for filename in os.listdir(path):
        if filename.endswith('.bin'):
            file_paths.append(os.path.join(path, filename))
    return file_paths


def hex_string_to_bytes(hex_string):
    return decode(b''.join(hex_string.split()), 'hex')


def read_file(path):
    with open(path, 'rb') as fp:
        return fp.read()


def write_file(path, data):
    with open(path, 'wb') as fp:
        fp.write(data)


def main():
    for path in bin_file_paths('./server_files'):
        binary_name = os.path.basename(path)
        data = hex_string_to_bytes(read_file(path))
        write_file('binary_{}'.format(binary_name), data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
