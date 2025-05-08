# rock, paper, scissors

import random
 
# game choices
choices = ["rock", "paper", "scissors"]

# player choices
player_choice = input("Enter rock, paper, scissors!: ").lower()

# computer  choice
computer_choice = random.choice(choices)
#player decision
if player_choice == computer_choice:
    print(f"both are same choice {player_choice}. It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wwins! {player_choice} beats {computer_choice}.")
    
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player wwins! {player_choice} beats {computer_choice}.")
    
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player wwins! {player_choice} beats {computer_choice}.")

else:
    print(f"Computer wins! {computer_choice} beats {player_choice}.")