#!/usr/bin/env python3
# Project Euler - Problem 50 - Consecutive Prime Sum

import time

# Sieve of Eratosthenes to generate primes
def getPrimes():
	primeBool = [True for i in range(1000000)]
	p = 2
	n = 999999
	while(p * p <= n):
		if(primeBool[p] == True):
			for i in range(p * p, n + 1, p):
				primeBool[i] = False
		p += 1
	primeNums = []
	for p in range(2, 1000000):
		if primeBool[p]:
			primeNums.append(p)
	return primeNums

# sum consecutive primes and store in an array
def sumPrimes(primes):
	storedSums = []
	curSum = 0
	for n in primes:
		curSum += n
		storedSums.append(curSum)
	return storedSums

start = time.time()
primes = getPrimes()
sums = sumPrimes(primes)
walk = 0
prime = 0

# loop through the sums array until you get the res
size = len(sums)
half = size//2
for i in range(size-1, -half, -1):
	for j in range(size):
		# if the resultant prime is >1000000, skip it
		if(sums[i] - sums[j] > 1000000):
			break
		# if they sum to a prime and there are more primes in the sum
		if((sums[i] - sums[j] in primes) and (i - j > walk)):
			walk = i - j
			prime = sums[i] - sums[j]
		if(j + 1 == i):
			break
			
end = time.time()	
print("%d is the sum of the most consecutive primes at %d" %(prime, walk))
print("Took %f seconds to run" %(end-start))
