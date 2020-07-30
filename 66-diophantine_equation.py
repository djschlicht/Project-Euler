#!/usr/bin/env python3
# Project Euler - Problem 66 - Diophantine Equation

import time
from math import sqrt
start = time.time()

# x^2 -D*y^2 = 1
# can solve by finding convergents of sqrt(n)
# p = x, q = y
# p_i = a_i * p_i-1 + p_i-2, p0 = a0 and p_-1 = 1
# q_i = a_i * q_i-1 + q_i-2, q0 = 1 and q_-1 = 0

xs = []
pmax = 0
res = 0
for D in range(2, 1001):
	# skip perfect squares
	l = int(sqrt(D))
	if l**2 == D: continue

	m, d, a = int(0), int(1), int(l)
	p1, p = int(1), int(a)	
	q1, q = int(0), int(1)
	while (p*p - D * q*q != 1):
		m = d * a - m
		d = int((D - m*m) // d)
		a = int((l + m) // d)
		
		p2 = (p1)
		p1 = (p)
		q2 = (q1)
		q1 = (q)		
		
		p = (a * p1 + p2)
		q = (a * q1 + q1)
	
	if p > pmax:
		pmax = p
		res = D

	print("D: %d\tx: %d" %(D,p))
	xs.append(p)
	
print("Largest x for is when D = %d" %(res))		
		
		
print("Runtime was %f seconds." %(time.time() - start))
