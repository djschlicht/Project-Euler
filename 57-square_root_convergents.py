#!/usr/bin/env python3
# Project Euler - Problem 57 - Square Root Convergents

import time
import math

start = time.time()

tally = 0
d = 2
n = 3

for i in range(0, 1000):
	n += 2 * d
	d = n - d
	if int(math.log10(n)) > int(math.log10(d)):
		tally += 1

print("The number of iters with more digits in the numerator is %d." %(tally))
print("Runtime was  %f seconds." %(time.time() - start))
