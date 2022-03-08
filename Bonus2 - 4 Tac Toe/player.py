import math
import random

class Player:
	def __init__(self, letter):
		# letter is x or o
		self.letter = letter

	# we want all players to get their next move given a game
	def get_move(self, game):
		pass

class RandomComputerPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		square = random.choice(game.available_moves())

		return square

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def _hex_dict(self, user_input):
		hex_lookup = {
			'a': 10,
	        'b': 11,
	        'c': 12,
	        'd': 13,
	        'e': 14,
	        'f': 15
		}
		if user_input in hex_lookup:
			return hex_lookup[user_input]
		else:
			return user_input


	def get_move(self,game):
		valid_square = False
		val = None
		while not valid_square:
			square = input(self.letter + '\'s turn. Input move (0-f):')
			# we're going to check that this is a correct value
			# check if it's an integer. If not, then say it's invalid
			# If the spot is not available, then invalid
			try:
				val = int(self._hex_dict(square))
				if val not in game.available_moves():
					raise ValueError
				valid_square = True # if these are successful, yay!
				
			except ValueError:
				print('Invalid square. Try again.')

		return val