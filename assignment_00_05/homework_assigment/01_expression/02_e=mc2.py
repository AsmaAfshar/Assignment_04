# Einstein's mass-energy equivalence calculator

# Constant speed of light in meters per second
C = 299792458  # m/s

while True:
    try:
        # Ask the user to enter mass in kilograms
        user_input = input("\nEnter kilos of mass (or type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break

        # Convert input to float
        m = float(user_input)

        # Calculate energy
        E = m * C**2

        # Display output
        print("\ne = m * C^2...\n")
        print(f"m = {m} kg")
        print(f"C = {C} m/s")
        print(f"{E} joules of energy!")

    except ValueError:
        print("Please enter a valid number for mass or type 'quit' to exit.")


# Enter kilos of mass (or type 'quit' to exit): 100

# e = m * C^2..

# m = 100.0 Kg
# C = 299792458 m/s
# 8.987551787368176e+18 joules of energy!
