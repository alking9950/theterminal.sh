#!/usr/bin/env python
from __future__ import print_function
import os
import sys

from codecs import decode


KEY = 'B105F00D'
INT_KEY = int(KEY, 16)


def xor(block):
    return '{:08X}'.format(int(block, 16) ^ INT_KEY)

def main():
    for filename in os.listdir('.'):
        if not filename.endswith('.bin'):
            continue
        print(filename)
        with open(filename) as fp:
            data = fp.read().split()

        output = ''
        xor_output = ''
        for block in data:
            if block == KEY:
                continue
            output += block
            xor_output += xor(block)

        with open('{}_plain'.format(filename), 'wb') as fp:
            fp.write(decode(output, 'hex'))

        with open('{}_xor'.format(filename), 'wb') as fp:
            fp.write(decode(xor_output, 'hex'))

    return 0


if __name__ == '__main__':
    sys.exit(main())
