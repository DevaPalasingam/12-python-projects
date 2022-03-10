import random

# lets create a board object to represent the minesweeper game
# this is so that we can say "create new board object"
# or "dig here", or "render this game for this object"
class Board:
	def __init__(self, dim_size, num_bombs):
		# keep track of these parameters. They'll be helpful
		self.dim_size = dim_size
		self.num_bombs = num_bombs

		# let's create the board
		# helper function
		self.board = self.make_new_board() # plant the bombs
		self.assign_values_to_board()

		# initialize a set to keep track of which locations uncovered
		# we'll save (row, col) tuples into this set
		self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

	def make_new_board(self):
		# construct a new board based on the dim size and num bombs
		# we should construct the list of lists here

		# generate a new board
		board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
		# this creates an array that looks like this:
		# [[None, None, ....., None],
		#  [None, None, ....., None],
		#  [....                   ],
		#  [None, None, ....., None]]
		# See how this represents a board

		# plant the bombs
		bombs_planted = 0
		while bombs_planted < self.num_bombs:
			loc = random.randint(0, self.dim_size**2 -1)
			# above returns a random int N such that a <= N <= b
			row = loc // self.dim_size
			col = loc % self.dim_size

			if board[row][col] == '*':
				# this means we've already planted a bomb there, so continue
				continue

			board[row][col] = '*' # plant the bomb
			bombs_planted += 1

		return board

	def 

# play the game
def play(dim_size=10, num_bombs=10):
	# Step 1: create the board and plant the bombs
	# Step 2: show the user the board and ask where they want to dig
	# Step 3a: if location is a bomb, show Game Over
	# Step 3b: if location is not a bomb, dig dig until each square is next to bomb
	# Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory!
	pass