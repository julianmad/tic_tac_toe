import random
print("papier, kamień i nożyce, gramy")
player_wins=0
computer_wins=0
winning_score = 5
while player_wins < winning_score and computer_wins < winning_score:
	print(f"Wynik komputera: {computer_wins}; wynik gracza: {player_wins}")
	
	player1 = input("Wybór gracza nr 1: ")
	if player1 == "exit" or player1 == "quit":
		break
	
	player2 = random.choice(["papier", "kamień", "nożyce"])
	print("Wybór komputera")
	print(player2)
	if player1 and player2:
		print("lecimy!")
		if player1 == player2:
			print("Remis")
		elif player1 == "kamień":
			if player2 == "nożyce":
				print("człowiek wygrywa")
				player_wins += 1
			elif player2 == "papier":
				print("komp wygrywa")
				computer_wins += 1
		elif player1 == "nożyce":
			if player2 == "kamień":
				print("komp wygrywa")
				computer_wins += 1
			elif player2 == "papier":
				print("człowiek wygrywa")
				player_wins += 1
		elif player1 == "papier":
			if player2 == "kamień":
				print("komp wygrywa")
				computer_wins += 1
			elif player2 == "nożyce":
				print("człowiek wygrywa")
				player_wins += 1														 	
	else:
		print("proszę wpisać swój wybór!!!")	
if player_wins > computer_wins:
	print("gratulacje człowieku, wygrałeś z maszyną!!!!!!")	
elif computer_wins == player_wins:
	print("REMIS, CIAOOO KAKAŁO")	
elif computer_wins > player_wins:
	print("KOmputer RULEZ")					
print(f"Wynik komputera: {computer_wins}; wynik gracza: {player_wins}")		