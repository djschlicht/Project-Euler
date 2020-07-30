#!/usr/bin/env python3
# Project Euler - Problem 56 - Powerful Digit Sum

import time

start = time.time()

# calculates the digit sum
def digitSum(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s
	
max_digital_sum = 0

for a in range(99, 0, -1):
	for b in range(99, 0, -1):
		num = a ** b
		t = digitSum(num)
		if t > max_digital_sum:
			max_digital_sum = t
			
print("The max digital sum is %d." %(max_digital_sum))
print("Runtime was %f seconds." %(time.time() - start))
