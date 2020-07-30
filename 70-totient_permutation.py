#!/usr/bin/env python3
# Project Euler - Problem 70 - Totient Permutation

import time
from math import sqrt

start = time.time()

# Sieve of Eratosthenes - generate primes from a to b
def get_primes(a, b):
	bools = [True for i in range(0, b + 1)]
	p = 2
	while(p * p <= b):
		if(bools[p] == True):
			for i in range(p * p, b + 1, p):
				bools[i] = False
		p += 1
	primes = []
	for p in range(a, b):
		if bools[p]:
			primes.append(p)
	return primes
	
# checks if 2 nums are a permutation of each other
def is_permutation(a, b):
	return sorted(str(a)) == sorted(str(b))
	
min_ratio = (10**7, 0)
primes = get_primes(1000, 7000)
for p1 in range(0, len(primes)):
	for p2 in range(p1 + 1, len(primes)):
		n = primes[p1] * primes[p2]
		if n > 10**7:
			break

		phi = (primes[p1] - 1) * (primes[p2] - 1)
		ratio = n / phi

		if is_permutation(n, phi) and ratio < min_ratio[0]:
			min_ratio = (ratio, n)


print("Min of permutations n / phi(n) = %f at n = %d" %(min_ratio[0], min_ratio[1]))
print("Runtime was %f seconds." %(time.time() - start))
