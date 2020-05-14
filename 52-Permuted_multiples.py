#!/usr/bin/env python3
# Project Euler - Problem 52 - Permuted Multiples

'''
It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order. Find the smallest 
positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import time

start = time.time()

# Check that 2 integers have the same digits. Returns true if they do.
def checkDigits(a, b):
	return sorted(str(a)) == sorted(str(b))
	
# Work through all the integers starting at 1
for x in range(10, 250000):
	if not checkDigits(x, x*2):
		continue
	if not checkDigits(x, x*3):
		continue
	if not checkDigits(x, x*4):
		continue		
	if not checkDigits(x, x*5):
		continue
	if not checkDigits(x, x*6):
		continue		
		
	print("The smallest integer with this property is %d" %(x))
	print("Runtime was %f seconds" %(time.time() - start))
