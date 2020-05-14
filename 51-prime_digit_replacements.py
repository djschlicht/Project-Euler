#!/usr/bin/env python3
# Project Euler - Problem 51 - Prime Digit Replacements

'''
By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all 
prime. By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the 
ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 
56663, 56773, and 56993. Consequently 56003, being the first member of 
this family, is the smallest prime with this property. Find the smallest
prime which, by replacing part of the number (not necessarily adjacent 
digits) with the same digit, is part of an eight prime value family.
'''

import time, math

primeNums = []
primeNums.append(2)
tempPrimes = []
wildcards = []
checkedPrimes = set()

# Sieve of Eratosthenes to generate primes
def getPrimes():
	primeBools = [True for i in range(1000000)]
	p = 2
	n = 999999
	while(p * p <= n):
		if(primeBools[p] == True):
			for i in range(p * p, n + 1, p):
				primeBools[i] = False
		p += 1
	for p in range(3, 1000000):
		if primeBools[p]:
			primeNums.append(p)
		
# generate the possible wildcard variations
def genWildcards(num, idx):
	if(idx > 0 and num not in checkedPrimes):
		wildcards.append(num)
		checkedPrimes.add(num)
	for x in range(idx, len(num)):
		genWildcards(putAsterisks(num, x), x + 1)
		
# put in asterisks
def putAsterisks(num, idx):
	return num[0:idx] + '*' + num[idx+1:]
	
# search the set of prime to see if num is prime (jump search)
def search(num):
	#setup
	n = len(primeNums)
	step = math.sqrt(n)
	prev = 0
	
	# finding the correct block
	while(primeNums[int(min(step, n)-1)] < num):
		prev = step
		step += math.sqrt(n)
		if(prev >= n):
			return -1
			
	# linear search in the block
	while(primeNums[int(prev)] < num):
		prev += 1
		if(prev == min(step, n)):
			return -1
	
	# if elem is found
	if(primeNums[int(prev)] == num):
		return prev
		
	return -1
	
# start timing
start = time.time()

# generate primes up to 1,000,000
getPrimes()

# iterate through the list of primes
for p in range(0, len(primeNums)):
	# generate the wildcards
	wildcards = []
	genWildcards(str(primeNums[p]), 0) 
	
	# iterate through the wildcards
	for w in range(1, len(wildcards)): 
		counter = 0
		tempPrimes.clear()
		# replace the * with integers [0, 9]
		for i in range(0, 10):
			num = int(wildcards[w].replace('*', str(i)))
			if(len(str(num)) < len(wildcards[w])):
				continue
			res = search(num)
			if(res >= 0):
				tempPrimes.append(num)
				counter += 1
			
		# if we found 0 in one go, then print results and exit
		if(counter >= 8):
			print("First prime in the 8-prime family is: %d" %(tempPrimes[0]))
			print(tempPrimes)
			end = time.time()
			print("Took %f seconds to run" %(end-start))
			exit(0)
				

