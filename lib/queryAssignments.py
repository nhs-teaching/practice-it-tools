import csv
import os
import sys

class Assignments:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../assignments.csv"
        with open(os.path.join(script_dir, rel_path), 'r') as assignment:
            self.reader = list(csv.DictReader(assignment))

    def countAssignments(self, unit):
        assignments = set()

        for problem in self.reader:
            if (problem['Unit'] == unit):
                assignments.add(problem['Homework'])

        return len(assignments)

    def getProblems(self, unit, hw):
        problems = []

        for problem in self.reader:
            if (problem['Unit'] == unit and problem['Homework'] == hw):
                problems.append(problem['Problem'])

        return problems

def main():
    a = Assignments()
    pl = a.getProblems("1", "1")
    print(pl)

    print(a.countAssignments("3"))


if __name__ == "__main__":
    main()
