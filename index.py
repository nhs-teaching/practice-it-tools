#!/usr/bin/env python

import sys
from optparse import OptionParser
from lib.loadResults import Results
from lib.queryAssignments import Assignments
from lib.queryStudents import Roster

def main():
    parser = OptionParser()
    # <period> <unit> <homework>
    parser.add_option("-n", "--names", action="store_true")

    (options, args) = parser.parse_args()

    assignments = Assignments()
    problems = assignments.getProblems(args[1], args[2])

    roster = Roster(args[0])
    roster.setupScoreSheet()

    results = Results(args[0])
    results.loadAll()

    for r in results.results:
        if r['Username'] in roster.scores and r['Problem'].split(':')[0] in problems:
            roster.scores[r['Username']].add(r['Problem'])

    grade_book_format = []
    for s in roster.scores:
        grade_book_format.append({
            'name' : roster.findByUsername(s)['Student'],
            'score': len(roster.scores[s])
        })

    for s in sorted(grade_book_format, key=lambda s : s['name']):
        if options.names:
            sys.stdout.write(s['name'] + " " + str(s['score']) + "\n")
        else:
            sys.stdout.write(str(s['score']) + "\n")

if __name__ == "__main__":
    main()
