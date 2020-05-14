#!/usr/bin/env python3
# Project Euler - Problem 53 - Combinatoric Selections

import time, math

start = time.time()

# Combination function
def combination(n, r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

count = 0
for n in range(23, 101):
	for r in range(1, n):
		if(combination(n, r) > 1000000):
			count += 1
			
print("There are %d values of nCr for 1<=n<=100 greater than 1000000" %(count))
print("Runtime was %f seconds" %(time.time() - start))
