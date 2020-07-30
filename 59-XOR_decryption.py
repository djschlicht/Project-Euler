#!/usr/bin/env python3
# Project Euler - Problem 59 - XOR Decryption

import time
from statistics import mode

start = time.time()

# Decrypts the text with provided key
def decrypt(text, key):
	out = []
	for i in range(0, len(text)):
		out.append(int(text[i]) ^ key[i%3])
	return out

# Does a frequency analysis of letters and returns correct key
def cryptanalysis(text):
	t1 = []
	t2 = []
	t3 = []
	# split text into pile for each char in key
	for c in range(len(text)):
		if c % 3 == 0:
			t1.append(text[c])
		if c % 3 == 1:
			t2.append(text[c])			
		if c % 3 == 2:
			t3.append(text[c])
			
	# get most common in each pile
	c1 = mode(t1)
	c2 = mode(t2)
	c3 = mode(t3)
	
	# most common should be ' ' (32), so convert into correct key
	k1 = int(c1) ^ 32
	k2 = int(c2) ^ 32
	k3 = int(c3) ^ 32
		
	return [k1, k2, k3]	
	

# Open the ciphertext file and get the ciphertext
f = open("p059_cipher.txt", "r")
ciphertext = f.readline().split(',')
f.close()

key = cryptanalysis(ciphertext)
plaintext = decrypt(ciphertext, key)
s = 0
for i in range(len(plaintext)):
	s += plaintext[i]

print("Sum of ascii in decrypted text: %d" %(s))

print("Runtime was %f seconds." %(time.time() - start))
