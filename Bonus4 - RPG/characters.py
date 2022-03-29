class Character:
	name = ""
	health = 0
	attack = 0
	defense = 0
	magic = 0
	description = ""

p1 = Character()
p1.name = "Ranger"
p1.health = 10
p1.attack = 3
p1.defense = 3
p1.magic = 0
p1.description = "Basic class, no particular strengths or weakness"

p2 = Character()
p2.name = "Tank"
p2.health = 15
p2.attack = 1
p2.defense = 5
p2.magic = 0
p2.description = "Can take hard hits, but doesn't hit very hard"

p3 = Character()
p3.name = "Healer"
p3.health = 8
p3.attack = 2
p3.defense = 3
p3.magic = 10
p3.description = "Helpful to others but not himself"

character_list = [p1,p2,p3]