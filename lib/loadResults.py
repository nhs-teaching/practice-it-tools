import csv
import os
import sys

from glob import glob

class Results:
    def __init__(self, period):
        self.period = period
        self.reset()

    def _load(self, file):
        with open(file, 'r') as chapter:
            self.results += list(csv.DictReader(chapter))

    def loadAll(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../results/p" + str(self.period) + "/c*.csv"

        files = glob(os.path.join(script_dir, rel_path))

        for f in files:
            self._load(f)

    def reset(self):
        self.results = []

def main():
    r = Results(2)
    r.loadAll()

    for attempt in r.results:
        print(attempt['Username'], attempt['Problem'])

if __name__ == "__main__":
    main()
