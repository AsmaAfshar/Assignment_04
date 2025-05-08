#Project:2 Guess the number game by computer
import random
def guess_the_number():
    number = random.randint(1, 100)
    guesses_left = 5
    # Welcome message
    print("Welcom to the number guessing game!")
    print("I'm thinking a number between 1 to 100")
    
    #loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess of another number."))
        except ValueError:
            print("Invalid input: Please enter a number")
            continue
        
        # Guess the secret number
        if guess < number:
            print("Too Low number. Tell anthor")
        elif guess > number:
            print("Too High number. Tell anthor")
        else:
            print(f"Congratulations! You Guess the Correct Number in {5 - guesses_left + 1 } tries.")
            return
        
        guesses_left -= 1
        # when all guess will be finished
        print(f"\nYou ran out of guess. The number was {number}.")
        
guess_the_number()
        
        