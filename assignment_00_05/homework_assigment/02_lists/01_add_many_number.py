#Problem Statement
#Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total



def sum_of_numbers(numbers)-> int:
    return sum(numbers)
my_list = [1, 2, 3, 4, 5]
result = sum_of_numbers(my_list)
print(result)  # Output: 15


