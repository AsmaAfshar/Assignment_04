

def get_last_element(lst):
    print("The last element is:", lst[-1])

# Prompt the user to input the number of elements
num_elements = int(input("Enter the number of elements in the list: "))

# Collect elements one by one
user_list = []
for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function with the user-provided list
get_last_element(user_list)
