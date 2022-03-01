# Pseudo code
# User types in if any of those letters are usable
# User types in if there's any bad letters
# Then will randomly select another 5 letter word with those letters

import random
from words import words
import string

alphabet = set(string.ascii_lowercase)

# Takes in good letters and bad letters from the user and list of all 5-letter words
# If there's no user input, will output a random word
# If there is user input letters, will output a list of words with those letters
def get_valid_word(good_letters, bad_letters, letter_placement, wordlist):
	if not good_letters and not bad_letters:
		random_word = random.choice(wordlist)
		print(random_word)
		return

	if not good_letters:
		random_word = random.choice(wordlist)
		while not set(random_word).isdisjoint(bad_letters):
			random_word = random.choice(wordlist)
		print(random_word)
		return

	for word in wordlist:
		if set(word).issuperset(good_letters) and set(word).isdisjoint(bad_letters):
			if compare_words(letter_placement, word):
				print(word)

# Checks the placed words (a--e-) and the word from the list
# Returns true if it fits and false if it doesn't
def compare_words(placed_letters, check_word):
	if not placed_letters:
		placed_letters = '-----'

	for count, letter in enumerate(check_word):
		if placed_letters[count] == '-':
			continue
		if placed_letters[count] != letter:
			return False
	return True

# Future development-------------------------------------------
# def hasRepeatedChars(s):
# 	for i in xrange(len(s)):
# 		if i != s.rfind(s[i]):
# 			return True
# 	return False
# def wrong_place(bad_letters, check_word):
	# input ex: b23c15
	# Need to separate out groupings b23 c15
	# Then need to compare each grouping to check_word
# Future development-----------------------------------------

def wordle():
	good_letters = input('Type any good letters you have found:\n').lower()
	bad_letters = input('Know any bad letters?\n').lower()
	letter_placement = input('Place your letters: eg (af-e-) \n')
	get_valid_word(set(good_letters), bad_letters, letter_placement, words)

wordle()