import random

words = ["hello", "world", "how", "why", "when", "what", "dormitory", "president", "city", "craziness", "girlfriend"]


difficulty = input("how hard do you want it to be?\ntype 1 for easy, type 2 for medium, type 3 for hard\n")

if difficulty == "1":
	lifes_left = 8
elif difficulty == "2":
	lifes_left = 4
elif difficulty == "3":
	lifes_left = 2
else:
	difficulty = input("how hard do you want it to be?\ntype 1 for easy, type 2 for medium, type 3 for hard\n")

word_chosen = random.choice(words)
player_word = []
split_word = [i for i in word_chosen]

for i in range(len(word_chosen)):
	player_word.append("_")
	
while(True):
		
	if "".join(player_word) == word_chosen:
		print("you won!")
		break
	if lifes_left == 0:
		print("you lose!")
		break
	else:
		g_letter = input("guess a letter\n")
		if g_letter in split_word:
			for i in range(len(word_chosen)):
				if g_letter == word_chosen[i] :
					player_word[i] = word_chosen[i]
					print("you guessed it right!!!!\nyou have {} lives left".format(lifes_left))
					print("".join(player_word))
		else:
			lifes_left -= 1
			print("you have guessed wrong!\nyou have {} lives left".format(lifes_left))


