#!/usr/bin/env python3
# Project Euler - Problem 71 - Ordered Fractions

import time

start = time.time()
	
a, b = 3, 7
r, s = 0, 1
bound = 2
q = 1000000
while q >= bound:
	p = (a * q - 1) // b
	if p * s > r * q:
		s = q
		r = p
		bound = s // (a * s - b * r)
	q -= 1

print("The fraction to the left of 3/7 is %d/%d" %(r, s))
print("Runtime was %f seconds." %(time.time() - start))
