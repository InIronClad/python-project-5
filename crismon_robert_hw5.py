#Assignment: (Homework #5)
#
#Description: (Rock Paper Scissors Game)
#
#Author: (Robert Crismon)
#
#Completion Time: (3 hours)
#
#In completing this program, I obtained help or worked with the following:
#(http://www.sourcecodester.com/tutorials/python/6771/how-create-rock-paper-scissors-game-python.html)

from random import *

player_choice = ''
player_weapon = ''
computer_choice = 0
r_count = 0
p_count = 0
s_count = 0
player_score = 0
computer_score = 0
ties = 0

print("Rock, Paper, Scissors!")
#while the player has not quit the game
while player_choice != "q":

	#if the player has chosen r, p, or s as their
	#preferred strategy
	if r_count > p_count + 2 and r_count > s_count + 2:
		player_weapon = "r"
		if player_weapon == "r":
			computer_choice = "p"
	elif p_count > r_count + 2 and p_count > s_count + 2:
		player_weapon = "p"
		if player_weapon == "p":
			computer_choice = "s"
	elif s_count > p_count + 2 and s_count > r_count + 2:
		player_weapon = "s"
		if player_weapon == "s":
			computer_choice = "r"
		
	#when the player hasn't shown to have chosen a strategy
	else:
		computer_choice = randint(0,2)
		if computer_choice == 0:
			computer_choice = "r"
		elif computer_choice == 1:
			computer_choice = "p"
		elif computer_choice == 2:
			computer_choice = "s"
			
	#player inputs choice here
	player_choice = input("Choose (r)ock, (p)aper, (s)cissors, or (q)uit: ")
	#if the player tries to input something other than r, p, s, or q
	if player_choice != "r" and player_choice != "p" and player_choice != "s" and player_choice != "q":
		print("Invalid choice! please choose either (r)ock, (p)aper, or (s)cissors to play.")
		print("Otherwise, enter (q)uit to end the game.")
		
	#if the player selected rock	
	elif player_choice == "r":
		r_count += 1
		if computer_choice == "s":
			print("The computer chooses scissors. You win!")
			player_score += 1
		elif computer_choice == "p":
			print("The computer chooses paper. You lose")
			computer_score += 1
		elif player_choice == computer_choice:
			print("It's a tie!")
			ties += 1
			
	#if the player selected paper		
	elif player_choice == "p":
		p_count += 1
		if computer_choice == "r":
			print("The computer chooses rock. You win!")
			player_score += 1
		elif computer_choice == "s":
			print("The computer chooses scissors. You lose")
			computer_score += 1
		elif player_choice == computer_choice:
			print("It's a tie!")
			ties += 1
			
	#if the player selected scissors	
	elif player_choice == "s":
		s_count += 1
		if computer_choice == "p":
			print("The computer chooses paper. You win!")
			player_score += 1
		elif computer_choice == "r":
			print("The computer chooses rock. You lose")
			computer_score += 1
		elif player_choice == computer_choice:
			print("It's a tie!")
			ties += 1

#if the player quits the game			
else:
	print("Game over.")
	print("Computer wins:", computer_score)
	print("Player wins:", player_score)
	print("Ties:", ties)
	print("Rock selected", r_count, "times")
	print("Paper selected", p_count, "times")
	print("Scissors selected", s_count, "times")
	