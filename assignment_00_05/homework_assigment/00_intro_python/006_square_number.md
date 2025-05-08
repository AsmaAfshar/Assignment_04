Problem Statement
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0

# Ask the user for a number
num = float(input("Type a number to see its square: "))

# Calculate the square of the number
square = num * num

# Print the result
print(f"{num} squared is {square}")

Type a number to see its square: 4
4.0 squared is 16.0


solution

num = 8
square = num * num
print(f"{num} square is {square}")

#output
8 square is 64