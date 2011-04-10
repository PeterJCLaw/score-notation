#!/usr/bin/env python

import urllib
import parser
import sys

match = sys.argv[1]
match = int(match)

page = urllib.urlopen('http://isburning.me/srobomatches/%d.txt' % match)

print 'T\tScore'
for line in page.readlines():
	team, string = line.split(' ')
	score = parser.fsm(string)
	print '%s\t%s\t%s' % (team, score, string.strip())

