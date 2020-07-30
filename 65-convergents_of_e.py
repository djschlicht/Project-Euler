#!/usr/bin/env python3
# Project Euler - Problem 65 - Convergents of e

import time
import math

start = time.time()

e = [2]
k = 1
for i in range(2, 102):
	if (i % 3 == 0):
		e.append(2 * k)
		k += 1
	else:
		e.append(1)

# convergent = p/q where p_i = a_i*p_i-1 + p_i-2
n1 = 1
n2 = 2
ns = [2]
print(e[2])
for i in range(2, 101):
	n = n2 * e[i-1] + n1
	ns.append(n)
	n1 = n2
	n2 = n
	
digit_sum = 0
for digit in str(int(ns[99])):
	digit_sum += int(digit)
print(digit_sum)

print("Runtime was %f seconds." %(time.time() - start))
