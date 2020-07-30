#!/usr/bin/env python3
# Project Euler - Problem 

import time
from math import sqrt, floor

start = time.time()

odd = 0

# Note: this method doesn't work for some integers. idk why.
def continued_fraction(num):
	period = 0
	first = int(num)
	cf = [first]
	frac = num - first
	integer = 0
	if frac != 0:	
		while integer != 2 * first:
			frac = 1 / frac
			integer = int(frac)
			frac = frac - integer
			cf.append(integer)
			period += 1
	return period

# checks if n is a perfect square (needs math library)
def is_square(n):
	sr = sqrt(n)
	return ((sr - floor(sr)) == 0)
	
def continued_fraction_fixed(num):
	m = 0.0
	d = 1.0
	a0 = int(sqrt(num))
	an = int(sqrt(num))
	period = 0
	if a0 != sqrt(num):
		while an != 2*a0:
			m = d*an-m
			d = (num - m**2)/d
			an = int((a0 + m)/d)
			period+=1
	return period
	
for n in range(2, 10001):
	period = continued_fraction_fixed(n) 
	print("n: %d\tperiod: %d" %(n, period))
	if (period + 1) % 2 == 0:
		odd += 1


print("There are %d continued fractions under 10000 with odd periods." %(odd))
	

print("Runtime was %f seconds." %(time.time() - start))
