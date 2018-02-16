#!/usr/bin/env python
from __future__ import print_function
import requests
import sys
import time

HOST = 'http://theterminal.sh'


def run_command(command):
    response = requests.get('{}/repl?command={}'.format(HOST, command))
    if response.status_code == 503:
        time.sleep(0.5)
        return run_command(command)

    print('{} {} ETAG: {}'.format(response.status_code, response.request.url,
                                  response.headers.get('etag', 'NONE')))
    if response.status_code == 200:
        if response.text != '<p>command not found.</p>':
            print(repr(response.text))
    return response


def main():
    run_command('su+root')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_command(' '.join(sys.argv[1:]))
        sys.exit(0)
    sys.exit(main())
