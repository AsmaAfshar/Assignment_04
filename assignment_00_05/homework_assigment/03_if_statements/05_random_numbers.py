# Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer 
# in the range set by the parameters (inclusive). For example this call would produce a random 
# integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)
import random

NATURAL_NUMBERS:int = 10
MIN_VAL:int = 2
MAX_VAL:int = 100
def main():
    for _ in range(NATURAL_NUMBERS):
        number = random.randint(MIN_VAL, MAX_VAL)
        print(number, end=' ')
    print()  # Optional: adds a newline after printing
    
if __name__ == '__main__':
    main()
    
# 2nd method
#import random

#def main():
    #for _ in range(10):
        #number = random.randint(1, 100)
        #print(number, end=' ')

#if __name__ == '__main__':
    #main()
