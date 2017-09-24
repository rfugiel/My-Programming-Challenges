#Radomir Fugiel

import sys

def is_anagram(word1, word2):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for let in alpha:
		freq1 = word1.count(let)
		freq2 = word2.count(let)
		if freq1 != freq2:
			return False
	return True



for line in sys.stdin:
		curr = [x for x in line.strip().split('"') if len(x)>0]

		if is_anagram(curr[0].lower(), curr[2].lower()):
			print "Valid Pattern"
		else:
			print "Invalid Pattern"

