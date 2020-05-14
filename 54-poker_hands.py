#!/usr/bin/env python3
# Project Euler - Problem 54 - Poker Hands

import time

start = time.time()

cardDict = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8,'7':7, 
	'6':6, '5':5, '4':4, '3':3, '2':2}
p1_wins = 0
p2_wins = 0

# sorting function for hands of cards
def sort(hand):
	# get hand into a list 
	arr = hand.split()		
	
	# selection sort
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			s = arr[min_idx]
			t = arr[j]
			if cardDict.get(s[0]) > cardDict.get(t[0]):
				min_idx = j;
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr	 
	
# determines what kind of hand it is and returns a string token
def analyzeHand(hand):
	# Format of score array:
	# idx 0 -> straight, idx 1 -> flush, idx 2-5 -> pairs
	# idx 6-10 -> the cards in descending order
	scoreArr = ['0']*11

	# sort the hand
	hand = sort(hand)
		
	#### Information collecting about the hand itself.
	
	# Check for straight. RF special case where high card is A.
	straight = True
	for c in range(0, len(hand)-1):
		if cardDict.get(hand[c+1][0]) - cardDict.get(hand[c][0]) != 1:
			straight = False
	if straight:
		scoreArr[0] = 'S'		
				
	# Check for flush
	flush = True
	for c in range(0, len(hand)-1):
		if hand[c][1] != hand[c+1][1]:
			flush = False 
	if flush:
		scoreArr[1] = 'F'
	
	# Calculate matching pairs
	for c in range(0, len(hand)-1):
		if hand[c][0] == hand[c+1][0]:
			scoreArr[c+2] = hand[c][0]
			
	# Adding hand in descending order
	for c in range(0, len(hand)):
		scoreArr[c+6] = hand[4-c][0]
	
	return scoreArr
		
# a function for handling the scoring system
def pointHandler(hand1, hand2):
	global p1_wins
	global p2_wins
	
	# Format of score array:
	# idx 0 -> straight, idx 1 -> flush, idx 2-5 -> pairs
	# idx 6-10 -> the cards in descending order
	p1 = analyzeHand(hand1)
	p2 = analyzeHand(hand2)
	
	points_1 = score(p1)
	points_2 = score(p2)
	
	''' Debugging print statements
	print(hand1)
	print("P1 score: %d" %(points_1))
	print(p1)
	print("--------------")
	print(hand2)
	print("P2 score: %d" %(points_2))
	print(p2)	
	'''
	
	if points_1 > points_2:
		p1_wins += 1
	if points_1 < points_2:
		p2_wins += 1
		
	# TODO: Actually code in what it's supposed to be where a higher 
	# order card will win on a tie with like pairs and stuff...	
	# tie breaker	
	if (points_1 == points_2):
		for c in range(6, 11):
			if(cardDict.get(p1[c]) > cardDict.get(p2[c])):
				p1_wins += 1
				break
			if(cardDict.get(p1[c]) < cardDict.get(p2[c])):
				p2_wins += 1
				break
		
	

# a function to run the score through
def score(arr):	
	
	# royal flush
	if(arr[0] == 'S' and arr[1] == 'F' and arr[6] == 'A'):
		return 90
		
	# SF
	if arr[0] == 'S' and arr[1] == 'F':
		return 80
		
	# 4 of a kind 
	if ((arr[2] == arr[3] == arr[4] != '0' and arr[5] == '0') or 
	(arr[3] == arr[4] == arr[5] != '0' and arr[2] =='0')):
		return 70
		
	# full house
	if ((arr[2] == arr[3] != '0' and arr[5] != '0') or
	 (arr[2] != '0' and arr[4] == arr[5] != '0')):
		return 60
	
	# flush
	if arr[1] == 'F':
		return 50
	
	# straight
	if arr[0] == 'S':
		return 40
		
	# 3 of a kind
	if (arr[2] == arr[3] != '0' or arr[3] == arr[4] != '0' or arr[4] == arr[5] != '0'):
		return 30
		
	# 2 pair
	if((arr[2] != '0' and arr[4] != '0') or (arr[2] != '0' and arr[5] != '0') or
	(arr[3] != '0' and arr[5] != '0')):
		return 20
		
	# 1 pair
	if(arr[2] != '0' or arr[3] != '0' or arr[4] != '0' or arr[5]!= '0' ):
		return 10
		
	return 0
			
	
# open the text file
f = open("poker_hands.txt", "r")

# loop to read the file line by line
for i in range(0, 1000):
	line = f.readline()
	
	# split the line into their hands
	player1_hand = line[:len(line)//2]
	player2_hand = line[len(line)//2:]
	
	''' Test hands for scoring
	RF = 'AS KS QS JS TS' 
	FK = '2S 2D 2C 2H 3S'
	FH = 'KS KC QS QH QD'
	FL = 'TH 9H 8H 5H 3H'
	ST = '2C 3D 4S 5H 6H'
	TK = '2C 2D 2H AS JC'
	TP = '5H 5D 6S 6D 3C'
	OP = 'KS KC 2S 4H 6D'
	'''
	
	pointHandler(player1_hand, player2_hand)
	
print("P1's total wins: %d" %(p1_wins))
print("P2's total wins: %d" %(p2_wins))
f.close()
print("Runtime was %f seconds." %(time.time() - start))
