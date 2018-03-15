#!/usr/bin/env python
# Author: Bryce Boe (bboe)
from __future__ import print_function
import requests
import sys
import time

from html2text import html2text

HOST = 'http://theterminal.sh'


def run_command(command, force_output=False):
    response = requests.get('{}/repl?command={}'.format(HOST, command))
    if response.status_code == 503:
        time.sleep(0.5)
        return run_command(command)

    print('{} {}'.format(response.status_code, response.request.url))
    print('ETAG: {}'.format(response.headers.get('etag', '')))
    if response.status_code == 200:
        if force_output or response.text != '<p>command not found.</p>':
            print('---')
            formatted = html2text(response.text).strip().replace('\n\n', '\n')
            print(formatted)
    return response


def main():
    run_command('su+root')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_command(' '.join(sys.argv[1:]), force_output=True)
        sys.exit(0)
    sys.exit(main())
