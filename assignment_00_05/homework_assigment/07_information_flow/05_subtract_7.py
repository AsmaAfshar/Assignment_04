# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() 
# method to call the subtract_seven helper function! If you're stuck, revisit the 
# add_five example from lecture.

'''def main():
	num: int = 7
	num = subtract_seven(num)
	print("this should be zero: ", num)

def subtract_seven(num):
	num = num - 7
	return num


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()'''
    
    # 2nd method
    
def subtract_seven(num):
    return num - 7

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)

# Call the main function
main()
