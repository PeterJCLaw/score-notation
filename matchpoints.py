#!/usr/bin/env python

import urllib
import parser
import sys

def getScore(match):
	page = urllib.urlopen('http://isburning.me/srobomatches/%s.txt' % match)

	for line in page.readlines():
		team, string = line.strip().split(' ')
		score = parser.fsm(string)
		yield (team, score, string)

if __name__ == '__main__':
	match = sys.argv[1]
	print 'Match %s' % match
	print 'T\tScore'
	for info in getScore(match):
		print '%s\t%s\t%s' % info
