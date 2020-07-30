#!/usr/bin/env python3
# Project Euler - Problem 55 - Lychrel Numbers

import time

start = time.time()

# determines if a number is a palindrome or not
def isPalindrome(num):
	# look at the first digit and last digit and compare then
	# then move in until you reach the middle
	s = str(num)
	for i in range(0, len(s)//2):	
		if s[i] != s[len(s)-1-i]:
			return False;		
	return True

# reverses the order of a numbers digits
def flip(num):
	s = str(num)
	rev = ''
	for i in range(0, len(s)):
		rev += s[len(s)-1-i]
	return int(rev)

	
lychrel_nums = 0

# reverse and add numbers from 10 to 10000 
for n in range(10, 10000):
	# iterations won't go above 50
	for i in range(0, 50):
		n = n + flip(n)
		if isPalindrome(n):
			break
	if not isPalindrome(n):
		lychrel_nums += 1
		
print("There are %d Lychrel numbers <10000" %(lychrel_nums))
print("Runtime was %f seconds" %(time.time() - start))
