import random

def roll():
	return random.randint(1,6) + random.randint(1,6)
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
num = 100000
for x in range(num):
	dice = roll()
	if dice == 2:
		two +=1
	if dice == 3:
		three +=1
	if dice == 4:
		four +=1
	if dice == 5:
		five +=1
	if dice == 6:
		six +=1
	if dice == 7:
		seven +=1
	if dice == 8:
		eight +=1
	if dice == 9:
		nine +=1
	if dice == 10:
		ten +=1
	if dice == 11:
		eleven +=1
	if dice == 12:
		twelve +=1

print(f"Two: {two}")
print(f"Three: {three}")
print(f"Four: {four}")
print(f"Five: {five}")
print(f"Six: {six}")
print(f"Seven: {seven}")
print(f"Eight: {eight}")
print(f"Nine: {nine}")
print(f"Ten: {ten}")
print(f"Eleven: {eleven}")
print(f"Twelve: {twelve}")
print('')