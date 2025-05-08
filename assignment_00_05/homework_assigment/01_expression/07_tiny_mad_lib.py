# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, 
# and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time,
# and the words are eventually filled into the blanks of a word template to make
# an entertaining story! We've provided you with the beginning of a sentence 
# (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

#SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

#def main():
    # Get the three inputs from the user to make the adlib
    #adjective: str = input("Please type an adjective and press enter. ")
    #noun: str = input("Please type a noun and press enter. ")
    #verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    #print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")



# There is no need to edit code beyond this point

#if __name__ == '__main__':
    #main()
    
    
def mad_lib_game():  
    QUOTE_1: str = "Code in Place is fun. I learned to program and used Python to make my"
# Get inputs from the user
    adjective:str = input("Please type an adjective and press enter. ")
    noun:str = input("Please type a noun and press enter. ")
    verb:str = input("Please type a verb and press enter. ")

# Construct and print the final sentence
    final_sentence = f"{adjective} {noun} {verb}!"
    print(final_sentence)
    print(QUOTE_1 + " " + adjective + " " + noun + " " + verb + "!")

# Call the function to run the game
mad_lib_game()



def mad_lib_game():  
    QUOTE_1: str = "Code in Place is fun. I learned to program and used Python to make my"
    
    # First round of inputs
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # New inputs for second sentence
    place: str = input("Please type a place and press enter. ")
    adverb: str = input("Please type an adverb and press enter. ")
    
    # Build sentences
    sentence_1 = QUOTE_1 + " " + adjective + " " + noun + " " + verb + "!"
    sentence_2 = f"It happened in {place}, and it all unfolded {adverb}."

    # Print the story
    print("\nYour Mad Libs story:")
    print(sentence_1)
    print(sentence_2)

# Run the game
mad_lib_game()

