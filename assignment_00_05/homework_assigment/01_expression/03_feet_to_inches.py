#Problem Statement
#Converts feet to inches. Feet is an American unit of measurement.
#There are 12 inches per foot. Foot is the singular, and feet is the plural.


"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
    
    
    """
An example program with constants
"""

KM_IN_MILE: float = 1.60934  # Conversion factor. There are approximately 1.60934 kilometers in 1 mile.

def main():
    miles: float = float(input("Enter number of miles: "))  # Get the number of miles, cast it to a float
    kilometers: float = miles * KM_IN_MILE  # Perform the conversion
    print("That is", kilometers, "kilometers!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
