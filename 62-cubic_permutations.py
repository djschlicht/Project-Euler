#!/usr/bin/env python3
# Project Euler - Problem 62 - Cubic Permutations

import time

start = time.time()
	
cubes = []
for n in range(0, 10000):
	cube = sorted(list(str(n * n * n)))
	cubes.append(cube)
	if cubes.count(cube) == 5:
		print("Cube with 5 cubic permutations is: %d" %(cubes.index(cube)**3))
		break

print("Runtime was %f seconds." %(time.time() - start))
