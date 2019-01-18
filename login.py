#!/usr/bin/env python

import os
import requests
import sys

from optparse import OptionParser

def _getCourseId(period):
    OFFSET = 1391
    return str(OFFSET + int(period))

def _getChapterId(chapter):
    OFFSET = 246

    val = OFFSET + int(chapter)
    if (int(chapter) > 3):
        return str(val + 1)
    else:
        return str(val)

class PracticeitAPI:
    def __init__(self):
        self.session = requests.session()

    def login(self, uname, passwd):
        login_url = "https://practiceit.cs.washington.edu/login"

        login_payload = {
            "usernameoremail" : uname,
            "password" : passwd
        }
        self.session.post(login_url, data=login_payload, headers=dict(referer=login_url))

    def _fetchResults(self, period, chapter):
        url = "https://practiceit.cs.washington.edu/teacher/download-results"

        data_payload = {
            "courseid" : _getCourseId(period),
            "categoryid[]" : _getChapterId(chapter),
            "format" : "long",
            "includeattempts" : "on"
        }

        return self.session.get(url, params = data_payload, headers = dict(referer = url))

    def _cacheResults(self, data, file):
        with open(file, 'w') as output:
            output.write(data.content.decode('utf-8'))

    def fetchAndCacheResults(self, period, chapter):
        results = self._fetchResults(period, chapter)
        output = 'results/p' + str(period) + '/c' + str(chapter) + '.csv' 
        self._cacheResults(results, output)

def main():
    parser = OptionParser()
    # <period> <chapter>
    (options, args) = parser.parse_args() 

    api = PracticeitAPI()
    api.login(os.environ.get('PRACTICEIT_UNAME'), os.environ.get('PRACTICEIT_PW'))
    api.fetchAndCacheResults(args[0], args[1])


if __name__ == "__main__":
    main()
