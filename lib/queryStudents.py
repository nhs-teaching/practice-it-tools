import csv
import os
import sys

class Roster:
    def __init__(self, period):
        self.period = period

        script_dir = os.path.dirname(__file__)
        rel_path = "../roster/p" + str(self.period) + ".csv"

        with open(os.path.join(script_dir, rel_path)) as students:
            self.results = list(csv.DictReader(students))

    def findByUsername(self, username):
        for student in self.results:
            if student['Practice-it'] == username:
                return student

    def setupScoreSheet(self):
        self.scores = dict()

        for student in self.results:
            self.scores[student['Practice-it']] = set()

def main():
    r = Roster(1)
    print(r.findByUsername(sys.argv[1]))


if __name__ == "__main__":
    main()
