from player import HumanPlayer, RandomComputerPlayer
import time
import queue

class TicTacToe:
	move_counter = 0
	move_queue = queue.Queue()

	def __init__(self):
		self.board = [' ' for _ in range(16)] # we will use a single list to rep 4x4 board
		self.current_winner = None # keep track of winner!
	
	def print_board(self):
		# this is just getting the rows
		for row in [self.board[i*4:(i+1)*4] for i in range(4)]:
			print ('| ' + ' | '.join(row) + ' |')

	@staticmethod
	def print_board_nums():
		# 0 | 1 | 2 etc (tells us what hex number corresponds to what box)
		number_board = [[str(hex(i))[2:] for i in range(j*4, (j+1)*4)] for j in range(4)]
		for row in number_board:
			print('| ' + ' | '.join(row) + ' |')

	def available_moves(self):
		return [i for i, spot in enumerate(self.board) if spot == ' ']

	def empty_squares(self):
		return ' ' in self.board

	def num_empty_squares(self):
		return self.board.count(' ')

	def remove_move(self, square):
		self.board[square] = ' '

	def make_move(self, square, letter):
		# if valid move, then make move (assign square to letter)
		# then return true. if invalid, return false
		if self.board[square] == ' ':
			self.board[square] = letter

			# Here we place remove_move
			if self.move_counter < 8:
				self.move_counter += 1
				self.move_queue.put(square)
			else:
				self.remove_move(self.move_queue.get())
				self.move_queue.put(square)

			if self.winner(square, letter):
				self.current_winner = letter
			return True
		return False

	def winner(self, square, letter):
		# winner if 4 in a row anywhere.. we have to check all of these
		# first check row
		row_ind = square // 4
		row = self.board[row_ind*4 : (row_ind + 1) * 4]
		if all([spot == letter for spot in row]):
			return True

		# check column
		col_ind = square % 4
		column = [self.board[col_ind+i*4] for i in range(4)]
		if all([spot == letter for spot in column]):
			return True

		# check diagonals
		# only if the square is an even number (0,2,4,6,8)
		# these are the only possible moves to win diagonal
		if square % 3 == 0 or square % 5 == 0:
			diagonal1 = [self.board[i] for i in [0,5,10,15]] #left to right diagonal
			if all([spot == letter for spot in diagonal1]):
				return True
			diagonal2 = [self.board[i] for i in [3,6,9,12]] #right to left diagonal
			if all([spot == letter for spot in diagonal2]):
				return True

		# if all of these fail
		return False
		
def play(game, x_player, o_player, print_game=True):
	# returns the winner of the game(the letter)! or None for a tie
	if print_game:
		game.print_board_nums()

	letter = 'X' # starting letter
	# iterate while game still has empty squares
	# don't need to worry about winner because we'll just return, which will break the loop
	while game.empty_squares():
		# get the move from the appropriate player
		if letter == 'O':
			square = o_player.get_move(game)
		else:
			square = x_player.get_move(game)

		# let's define a function to make a move
		if game.make_move(square, letter):
			if print_game:
				print (letter + f' makes a move to square {square}')
				game.print_board_nums()
				print('')
				game.print_board()
				print('') #just empty line

			if game.current_winner:
				if print_game:
					print(letter + ' wins!')
				return letter

			# after we made our move, we need to alternate letters
			letter = 'O' if letter == 'X' else 'X' # switches player

		# tiny break to make things easier to read
		time.sleep(0.2)

	if print_game:
		print('It\'s a tie')

if __name__ == '__main__':
	x_player = HumanPlayer('X')
	o_player = RandomComputerPlayer('O')
	t = TicTacToe()
	play(t, x_player, o_player, print_game=True)