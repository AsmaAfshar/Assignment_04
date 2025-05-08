#Problem Statement
#Write a program that doubles each element in a list of numbers. For example, if you start with this list:

#numbers = [1, 2, 3, 4]

#You should end with this list:

#numbers = [2, 4, 6, 8]

numbers:list [int] = [3, 6, 9, 12] # Creates a list of numbers
for n in range (len(numbers)):     # Loop through the indices of the list
   num_at_index = numbers[n]  # Get the element at index i in the numbers list
   numbers[n] = num_at_index * 2  # Set the element at index i to be equal to the previous element times 2
   
print(numbers*2)      # This should print the doubled list