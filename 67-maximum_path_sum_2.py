#!/usr/bin/env python3
# Project Euler - Problem 67 - Maximum path sum 2

import time

start = time.time()

# read the file and put the triangle into a 2d list
f = open("p067_triangle.txt", "r")
triangle  = []
for line in f:
	line = line.rstrip("\n")
	triangle.append(line.split(" "))
f.close()

lines = len(triangle)
largest = [0]*lines

for i in range(0, lines):
	largest[i] = int(triangle[lines-1][i])
	
for i in range(lines-2, -1, -1):
	for j in range(0,  i+1):
		largest[j] = int(triangle[i][j]) + max(largest[j], largest[j+1])

print(largest[0])
	
print("Runtime was %f seconds." %(time.time() - start))
