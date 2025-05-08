#In the Gregorian calendar, three criteria must be checked to identify leap years:

#The given year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is NOT a leap year; unless:
#The year is also evenly divisible by 400. Then it is a leap year.

#def main():
    # Get the year to check from the user
    #year = int(input('Please input a year: '))

    #if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        #if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            #if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                #print("That's a leap year!")
            #else:  # (Not divisible by 400)
                #print("That's not a leap year.")
        #else:  # (Not divisible by 100)
            #print("That's a leap year!")
    #else:  # (Not divisible by 4)
        #print("That's not a leap year.")


# There is no need to edit code beyond this point

#if __name__ == '__main__':
    #main()
    
    
    # 2nd method
def main():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
