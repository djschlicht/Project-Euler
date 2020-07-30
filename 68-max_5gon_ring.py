#!/usr/bin/env python3
# Project Euler - Problem 

import time
from itertools import permutations

start = time.time()

# outside ring is indices 0, 2, 4, 6, 8. inside ring is 1, 3, 5, 7, 9
ring = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = '0'

def check_rules(p):
	# check that larger nums are on outside
	if p[1] == 10 or p[3] == 10 or p[5] == 10 or p[7] == 10 or p[9] == 10:
		return False
	
	# check that starting point (index 1) is smallest out of outer
	if p[0] > p[2] or p[0] > p[4] or p[0] > p[6] or p[0] > p[8]:
		return False
		
	# check the sums of the lines for equality
	if((p[0] + p[1] + p[3] != p[2] + p[3] + p[5]) or
	   (p[0] + p[1] + p[3] != p[4] + p[5] + p[7]) or
	   (p[0] + p[1] + p[3] != p[6] + p[7] + p[9]) or
	   (p[0] + p[1] + p[3] != p[8] + p[9] + p[1])):
		   return False

	return True
	
# generate all permutations of the ring
for p in permutations(ring):
	p = list(p)
	# check that the permutation obeys the rules
	if check_rules(p):
		s = (str(p[0]) + str(p[1]) + str(p[3]) + str(p[2]) + str(p[3]) +
			str(p[5]) + str(p[4]) + str(p[5]) + str(p[7]) + str(p[6]) + 
			str(p[7]) + str(p[9]) + str(p[8]) + str(p[9]) + str(p[1]))
		if s > res:
			res = s

print("Maximum string is: " + res)
print("Runtime was %f seconds." %(time.time() - start))
