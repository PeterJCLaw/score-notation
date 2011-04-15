#!/usr/bin/env python

import sys
import matchpoints

NUM_MATCHES = 39

def getBestScores(num_matches):
	result = {}
	for match in range(1, num_matches):
		try:
			for score in matchpoints.getScore(match):
				points = score[1]
				if points not in result:
					result[points] = []

				result[points].append(score)
		except:
			pass

	return result

def getMatchResult(match):
	result = {}
	for score in matchpoints.getScore(match):
		points = score[1]
		if points not in result:
			result[points] = []

		result[points].append(score)

	return result

def printResult(result):
	print "Pos\tTeam\tScore\tString"
	pos = 1
	for points in sorted(result.iterkeys(), reverse=True):
		nTeams = 0
		position = result[points]
		for res in position:
			print "%d\t%s\t%s\t%s" % (pos, res[0], res[1], res[2])
			nTeams += 1
		pos += nTeams

if __name__ == '__main__':
	match = sys.argv[1]
	print "Results for match %s" % match
	res = getMatchResult(match)
	printResult(res)

	print "Best scores for all matches:"
	res = getBestScores(NUM_MATCHES)
	printResult(res)

