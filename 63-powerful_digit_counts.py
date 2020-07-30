#!/usr/bin/env python3
# Project Euler - Problem 63 - Powerful Digit Counts

import time
import math

start = time.time()

res = 0
low = 0
n = 1

while low < 10:
	low = int(math.ceil(10**((n-1)/n)))
	res += 10 -low
	n += 1

print("There are %d n-digit numbers which are also an nth power." %(res))

print("Runtime was %f seconds." %(time.time() - start))
