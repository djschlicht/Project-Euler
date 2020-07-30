#!/usr/bin/env python3
# Project Euler - Problem 58 - Spiral Primes

import time

start = time.time()

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

side_length = 7
num_primes = 8
diag_length = 13
cur_num = 49

while float(num_primes / diag_length) >= 0.1:
	
	#get new nums on the diags and check for primality
	for n in range(0, 4): 
		cur_num = cur_num + side_length + 1
		if isPrime(cur_num):
			num_primes += 1	
	
	#update diag_length
	diag_length += 4
	
	#update side_length
	side_length += 2


print("Side length when the prime ratio falls below 0.1 is %d." %(side_length))
print("Runtime was  %f seconds." %(time.time() - start))
