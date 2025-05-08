# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.

# Welcome to the High-Low Game!

# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
'''Your score is now 1

Round 2
Your number is 88
Do you think your number is higher or lower than the computer's?: higher
Aww, that's incorrect. The computer's number was 100
Your score is now 1

Round 3
Your number is 63
Do you think your number is higher or lower than the computer's?: higher
You were right! The computer's number was 5
Your score is now 2

Round 4
Your number is 57
Do you think your number is higher or lower than the computer's?: lower
Aww, that's incorrect. The computer's number was 57
Your score is now 2

Round 5
Your number is 22
Do you think your number is higher or lower than the computer's?: lower
Aww, that's incorrect. The computer's number was 1
Your score is now 2

Thanks for playing!'''


'''import random

NUM_OF_ROUNDS = 5
def game():
    print("Welcome to the High-Low game !")
    print("--------------------------------")
Your_Score = 0
for i in range(NUM_OF_ROUNDS):
    print("Round", i + 1)
    System_Num:int = random.randint(1, 100)
    Player_Num:int = random.randint(1, 100)
    print("Your number is", Player_Num)
    choice: str = input("Do you think your number is higher or lower than the system's?: ")
    higher_and_correct:bool = choice == "Higher" and Player_Num > System_Num
    lower_and_correct:bool = choice == "Lower"  and Player_Num < System_Num
    if higher_and_correct or lower_and_correct:
        print("You were right! The system's number was", System_Num)
        # Milestone 5: keep track of your score
        Your_Score += 1 
    else: 
        print("Aww, that's incorrect. The system's number was", System_Num)

        # Milestone 5: keep track of your score
    print("Your score is now", Your_Score)
    print()

print("Thanks for playing!") '''

               
import random

NUM_OF_ROUNDS = 5

def game():
    print("Welcome to the High-Low game!")
    print("--------------------------------")

    your_score = 0

    for round_number in range(1, NUM_OF_ROUNDS + 1):
        print(f"Round {round_number}")

        system_num = random.randint(1, 100)
        player_num = random.randint(1, 100)

        print("Your number is", player_num)
        choice = input("Do you think your number is Higher or Lower than the system's? (Type 'Higher' or 'Lower'): ").strip().capitalize()

        # Check the user's input
        if choice == "Higher":
            if player_num > system_num:
                print("You were right! The system's number was", system_num)
                your_score += 1
            else:
                print("Aww, that's incorrect. The system's number was", system_num)

        elif choice == "Lower":
            if player_num < system_num:
                print("You were right! The system's number was", system_num)
                your_score += 1
            else:
                print("Aww, that's incorrect. The system's number was", system_num)
        else:
            print("Invalid choice. Please type 'Higher' or 'Lower'. No points awarded this round.")

        print("Your score is now", your_score)
        print()

    print("Thanks for playing!")
    print("Your final score was:", your_score)

if __name__ == '__main__':
    game()

    