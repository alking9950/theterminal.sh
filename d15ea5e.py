#!/usr/bin/env python
# Author: Bryce Boe (bboe)
from __future__ import print_function
import json
import os
import re
import sys
import time

import requests


PATH_RE = re.compile("href='([^']+)'")
HOST = 'http://theterminal.sh'


def request(path):
    response = requests.get('{}{}'.format(HOST, path), allow_redirects=False)
    if response.status_code == 503:
            time.sleep(0.5)
            return request(path)

    if response.status_code != 302 \
       or response.headers['location'] != '/reboot.html':
        import pprint
        pprint.pprint(vars(response))
        print(response.request.url)
        sys.exit(1)

    print(response.request.url)


def disease_paths():
    response = requests.get('{}/repl?command=mem D15EA5E'.format(HOST))
    if response.status_code == 503:
        time.sleep(0.5)
        return disease_paths()
    assert response.status_code == 200
    return PATH_RE.findall(response.text)


def url_loop():
    for path in disease_paths():
        if '/reboot/' not in path:
            print(path)
            sys.exit(1)
        request(path)


def gather_data():
    FILENAME = 'disease_data.json'
    if os.path.isfile(FILENAME):
        with open(FILENAME) as fp:
            mapping = json.load(fp)
    else:
        mapping = {}

    second_numbers = set()
    for seconds in mapping.values():
        for second in seconds:
            if second in second_numbers:
                print('Duplicate: {}'.format(second))
            else:
                second_numbers.add(second)

    try:
        while True:
            for path in disease_paths():
                _, first, second = path.rsplit('/', 2)
                mapping.setdefault(first, []).append(second)
                if second in second_numbers:
                    print('Duplicate: {}'.format(second))
                else:
                    second_numbers.add(second)
            mapping[first] = sorted(mapping[first])
    except KeyboardInterrupt:
        pass
    except:
        import traceback
        traceback.print_exc()
        print('Saving...')
    with open('disease_data.json', 'w') as fp:
        json.dump(mapping, fp, indent=2, separators=(',', ': '),
                  sort_keys=True)


def main():
    gather_data()
    #  url_loop()


if __name__ == '__main__':
    sys.exit(main())
