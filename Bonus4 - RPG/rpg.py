# Pseudo code
# Set character stats as variables
# Player select characters
# Computer select characters
# Battle
# 	- Characters will randomly choose to either attack or use ability
# 	- If characters attack, they will randomly choose an opposing target
# 	- Display their choice
# 	- Each character on a team will take an action, then it's the other team's turn
# 	- Turns alternate until there's a winner

from characters import character_list

def show_characters():
	for x in character_list:
		print(x.name + " - " + x.description)

def check_characters(selected):
	if len(selected) != 3:
		print("Invalid input\n\n")
		return False
	return True

def play_game():
	print("Roster of characters:\n")
	show_characters()
	selected_characters = input("\nSelect 3 characters by typing their identifiers: \nEx. 2 Rangers + Tank = 'rrt'\n").lower()

	if check_characters(selected_characters):
		print("boboyeah")
	else:
		play_game()

play_game()