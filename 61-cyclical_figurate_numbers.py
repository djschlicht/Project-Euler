#!/usr/bin/env python3
# Project Euler - Problem 61 - Cyclical Figurate Numbers

import time

start = time.time()

# functions to generate each type of number
def triangle(n): return n * (n + 1) // 2
def square(n): return n * n
def pentagonal(n): return n * (3 * n - 1) // 2
def hexagonal(n): return n * (2 * n - 1)
def heptagonal(n): return n * (5 * n - 3) // 2
def octagonal(n): return n * (3 * n - 2)

# create a dict populated with the figurates
figs = {
	3: [n for n in map(triangle, list(range(1000))) if n < 10000 and n > 999],
	4: [n for n in map(square, list(range(1000))) if n < 10000 and n > 999],
	5: [n for n in map(pentagonal, list(range(1000))) if n < 10000 and n > 999],
	6: [n for n in map(hexagonal, list(range(1000))) if n < 10000 and n > 999],
	7: [n for n in map(heptagonal, list(range(1000))) if n < 10000 and n > 999],
	8: [n for n in map(octagonal, list(range(1000))) if n < 10000 and n > 999],
}

# check if 2 nums are cyclic
def is_cyclic(a, b):
	return str(a)[-2:] == str(b)[:2]
	
# iterate through all the permutations to find a cyclic chain
def find_cycle():
	numbers = [(key, value) for key in list(figs.keys()) for value in figs[key]]
	for k1, v1 in numbers:
		for k2, v2 in [(k, v) for k, v in numbers if k not in [k1] and is_cyclic(v1, v)]:
			for k3, v3 in [(k, v) for k, v in numbers if k not in [k1, k2] and is_cyclic(v2, v)]:
				for k4, v4 in [(k, v) for k, v in numbers if k not in [k1, k2, k3] and is_cyclic(v3, v)]:
					for k5, v5 in [(k, v) for k, v in numbers if k not in [k1, k2, k3, k4] and is_cyclic(v4, v)]:
						for k6, v6 in [(k, v) for k, v in numbers if k not in [k1, k2, k3, k4, k5] and is_cyclic(v5, v)]:
							if is_cyclic(v6, v1):
								return [v1, v2, v3, v4, v5, v6]
								
cycle = find_cycle()
print(cycle)
print("Sum of the cycle is: %d" %(sum(cycle)))
								
print("Runtime was %f seconds." %(time.time() - start))

