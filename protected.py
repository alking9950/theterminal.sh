#!/usr/bin/env python
# Author: Bryce Boe (bboe)
from __future__ import print_function
from itertools import permutations
import requests
import sys
import time

from html2text import html2text

HOST = 'http://theterminal.sh'


def request(path):
    response = requests.get('{}{}'.format(HOST, path))
    if response.status_code == 503:
        time.sleep(0.5)
        return request(path)
    if response.status_code != 200:
        print(response)
        sys.exit(1)
    return response


def current_state():
    response = request('/repl?command=mem%20write%20protected')
    text = html2text(response.text).strip().replace('\n\n', '\n').split('\n')
    data = ''.join(text[1:])
    return data


def bin_to_base2(data, alphabet='0Oo.'):
    quaternary = []
    for byte in data:
        quaternary.append(alphabet[byte >> 6])
        quaternary.append(alphabet[byte >> 4 & 3])
        quaternary.append(alphabet[byte >> 2 & 3])
        quaternary.append(alphabet[byte & 3])
    return ''.join(quaternary)


def terminal_format(data):
    while data:
        print(data[:32])
        data = data[32:]


def diff(desired, alphabet='0Oo.'):
    current = current_state()
    changes = 0
    for i, value in enumerate(desired):
        if value != current[i]:
            x, y = divmod(i, 32)
            print('Updating ({},{})'.format(x, y))
            server_value = None
            while server_value != value:
                server_value = request('/mem/write?bus={}&i={}'
                                       .format(x, y)).text
                changes += 1

    current = current_state()
    for index, value in enumerate(current[i + 1:]):
        while value != alphabet[0]:
            x, y = divmod(i + index + 1, 32)
            print('Zeroing ({},{}) {} -> {}'.format(x, y, value, alphabet[0]))
            value = request('/mem/write?bus={}&i={}'
                            .format(x, y)).text
            changes += 1
    return changes


def execute():
    response = request('/repl?command=mem exec protected')
    return html2text(response.text).strip().replace('\n\n', '\n')
    print(text)


def permute_B105F00D():
    """This function resulted only in INVALID PROGRAM :(."""
    data = b'\xb1\x05\xf0\x0d'
    for alphabet in permutations('0Oo.'):
        desired = bin_to_base2(data, alphabet)
        terminal_format(desired)
        changes = None
        while changes != 0:
            response = execute()
            if response != 'ERROR: INVALID PROGRAM':
                print(response)
                print('Alphabet: {}'.format(alphabet))
                terminal_format(current_state())
                return 0
            changes = diff(desired, alphabet)
            print(changes)



def main():
    #permute_B105F00D()
    data = sys.stdin.buffer.read()
    desired = bin_to_base2(data)
    terminal_format(desired)
    diff(desired)
    response = execute()
    if response != 'ERROR: INVALID PROGRAM':
        print(response)
        terminal_format(current_state())



if __name__ == '__main__':
    sys.exit(main())
