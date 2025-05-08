import random
words = ["tuples", "game", "java", "sets", "array"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcom to the hangman game!")
print(" _" * len(word))

while attempts > 0:
    guess = input("\n guess the letters: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("this letter is already guessed! please choose another letter")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1 
        print(f"Wrong {attempts} attempts.")
    displayed_words = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_words)
    if "_" not in displayed_words:
        print(f"Congratulation! the correct word is {word}")
else:
    print(f"Game Over! the correct word is {word}")    