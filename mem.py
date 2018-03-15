#!/usr/bin/env python
# Author: Bryce Boe (bboe)
from __future__ import print_function
import requests
import sys
import time

from html2text import html2text

HOST = 'http://theterminal.sh'


def mem(argument):
    response = requests.get('{}/repl?command=mem {}'.format(HOST, argument))
    if response.status_code == 503:
        time.sleep(0.5)
        return mem(argument)
    if response.status_code != 200:
        print(response)
        sys.exit(1)
    return html2text(response.text).strip().replace('\n\n', '\n')


def main():
    for i in range(0xB105F00D, 0xB105F00D + 200):
        result = mem(hex(i)[2:])
        if result == 'undefined':
            break
        print(result)


if __name__ == '__main__':
    sys.exit(main())
