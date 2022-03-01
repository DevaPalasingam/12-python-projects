import random

def play():
	user = input("Pick one: 'r' for rock, 'p' for paper, 's' for scissors\n")
	computer = random.choice(['r', 'p', 's'])

	if user == computer:
		return (f'Computer picked {computer}, It\'s a tie')

	if is_win(user, computer):
		return 	(f'Computer picked {computer}, You win!')

	return (f'Computer picked {computer}, You lose')

def is_win(player, opponent):
	# return true if player wins
	# r > s, s > p, p > r
	if (player == 'r' and opponent == 's') \
		or (player == 's' and opponent == 'p') \
		or (player == 'p' and opponent == 'r'):
		return True

print (play())