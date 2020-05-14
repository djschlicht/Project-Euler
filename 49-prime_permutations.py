#!/usr/bin/env python3
# Project Euler - Problem 49 - Prime permutation

# Get all the primes from 1000-9999 using sieve of eratosthenes
def getPrimes():
	# Sieve of Eratosthenes
	primeBool = [True for i in range(10000)]
	p = 2
	n = 9999
	while(p * p <= n):
		if(primeBool[p] == True):
			for i in range(p * p, n + 1, p):
				primeBool[i] = False
		p += 1
		
	# Get the actual numbers into a list and return it
	primeNums = []
	for p in range(1487, 10000):
		if primeBool[p]:
			primeNums.append(p)
	return primeNums

# checks for numerical permutations, if found returns true
def isPermutation(prime1, prime2):
		# sort the digits from low to high
		sp1 = "".join(sorted(str(prime1)))
		sp2 = "".join(sorted(str(prime2)))
		# check for equality
		if(int(sp1) == int(sp2)):
			return True
		else:
			return False

# Iterate through primes list for each prime
def checkPrimes(primes, n):
	perms = []
	perms.append(n)
	for p in primes:
		if(isPermutation(n, p)):
			perms.append(p)
	return perms

primes = getPrimes()
perms = []
idx = 1
for n in primes:
	perms = checkPrimes(primes[idx:], n)
	if(len(perms) == 3 and (perms[2]-perms[1] == perms[1]-perms[0])):
		break
	else:
		perms.clear()
		idx += 1

ans = str(perms[0]) + str(perms[1]) + str(perms[2])
print("Concatotnation of 4-digit prime permutations is " + ans)





