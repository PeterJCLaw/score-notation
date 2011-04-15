#!/usr/bin/env python

import urllib
import parser
import sys

match = sys.argv[1]
print 'Match %s' % match

page = urllib.urlopen('http://isburning.me/srobomatches/%s.txt' % match)

print 'T\tScore'
for line in page.readlines():
	team, string = line.strip().split(' ')
	score = parser.fsm(string)
	print '%s\t%s\t%s' % (team, score, string)

