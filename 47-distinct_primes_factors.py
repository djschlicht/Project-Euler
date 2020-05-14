#!/usr/bin/env python3
# Project Euler - Problem 47
# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these num0bers?

def foo(num_factors, num_sequence):
    limit = 10**9  # need to increase for highter vals of num
    factors = [0]*limit
    count = 0
    for num in range(2, limit):
        if factors[num] == num_factors:
            count += 1
            if count == num_sequence:
                s = num-num_sequence+1;
                seq = []
                for n in range(num_sequence):
                    seq.append(s)
                    s += 1
                print(seq)
                break
                count -= 1
        else:
            count = 0
            if factors[num] == 0:
                factors[num::num] = [x+1 for x in factors[num::num]]
    return

foo(2, 2)
foo(3, 3)
foo(4, 4)
