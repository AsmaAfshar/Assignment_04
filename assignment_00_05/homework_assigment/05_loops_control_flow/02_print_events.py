#Problem Statement
#Write a program that prints the first 20 even numbers. There are several correct
# approaches, but they all use a loop of some sort. Do no write twenty print statements
#The first even number is 0:
#0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

'''def even():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for e in range(20):
     print(e * 2)      # Use the 'e' value inside the for-loop
     
if __name__ == "__main__":
    even()'''
    
    #2nd method
    # Print the first 20 even numbers starting from 0
for i in range(20):
    print(i * 2, end=' ')
