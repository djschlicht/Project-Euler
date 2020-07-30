#!/usr/bin/env python3
# Project Euler - Problem 60 - Prime Pair Sets
'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two 
primes and concatenating them in any order the result will always be 
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The 
sum of these four primes, 792, represents the lowest sum for a set of 
four primes with this property. Find the lowest sum for a set of five 
primes for which any two primes concatenate to produce another prime.
'''

import time

start = time.time()

# Generates prime numbers up to n
def getPrimes(n):
	# Sieve of Eratosthenes
	primeBool = [True for i in range(n+1)]
	p = 2
	while(p * p <= n):
		if(primeBool[p] == True):
			for i in range(p * p, n + 1, p):
				primeBool[i] = False
		p += 1
	# Get the actual numbers into a list and return it
	primeNums = []
	for p in range(2, n):
		if primeBool[p]:
			primeNums.append(p)
	return primeNums

# determines if a number is prime
def isPrime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True	
	if (n % 2 == 0 or n % 3 == 0):
		return False	
	i = 5
	while(i * i <= n):
		if(n % i == 0 or n % (i + 2) == 0):
			return False
		i += 6
	return True
	
# Checks combined pairs for primality
def checkPairs(a, b):	
	return (isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a))))

# get first 10,000 prime numbers
primes = getPrimes(10000)

pairs = []
sum_primes = 0
# check the prime pairs until you get a group of 5
for a in primes:
	for b in primes:
		if b < a:
			continue
		if checkPairs(a, b):
			for c in primes:
				if c < b:
					continue
				if (checkPairs(a, c) and checkPairs(b, c)):
					for d in primes:
						if d < c:
							continue
						if (checkPairs(a, d) and checkPairs(b, d) 
						and checkPairs(c, d)):
							for e in primes:
								if e < d:
									continue
								if (checkPairs(a, e) and checkPairs(b, e)
								and checkPairs(c, e) and checkPairs(d, e)):
									pairs.append(a)
									pairs.append(b)
									pairs.append(c)
									pairs.append(d)
									pairs.append(e)
									sum_primes = a + b + c + d + e
									
print("Group of primes is:")
print(pairs)
print("Sum is %d" %(sum_primes))	

print("Runtime was %f seconds." %(time.time() - start))
