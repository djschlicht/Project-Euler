#!/usr/bin/env python3
# Project Euler - Problem 69 - Totient Maximum

import time
from math import sqrt

start = time.time()

# prime factorization - returns distinct primes
def prime_factorization(n):
	factors = [1]
	while n % 2 == 0:
		factors.append(2)
		n = n / 2
	for i in range(3, int(sqrt(n))+1, 2):
		while n % i == 0:
			factors.append(i)
			n = n / i
	return list(dict.fromkeys(factors))

# phi(n) = n * product(1 - 1/p) where p is distinct primes dividing n
# phi function - calculates phi(n)
def phi(n):
	factors = prime_factorization(n)
	p = n
	for f in factors[1:]:
		p *= (1 - 1/f)
	return p
	
# loop throuh n <= 1000000 and find max n/phi(n)
max_ratio = (0, 0)
for n in range(2, 1000001):
	p = phi(n)
	if (n/p) > max_ratio[0]:
		max_ratio = (n / p, n)
		
print("Max of n / phi(n) = %f at n = %d" %(max_ratio[0], max_ratio[1]))
print("Runtime was %f seconds." %(time.time() - start))
