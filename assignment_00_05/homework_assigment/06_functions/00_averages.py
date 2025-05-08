# Problem Statement
# Write a function that takes two numbers and finds the average between the two.

'''def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()'''
    
    
    # 2nd method
    
'''def average_of_two(num1, num2):
    return (num1 + num2) / 2
# Example
result = average_of_two(10, 20)
print("The average is:", result)'''

 #3rd method through user input
 
def average_of_two(num1, num2):
    return (num1 + num2) / 2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and display the average
average = average_of_two(num1, num2)
print("The average is:", average)

