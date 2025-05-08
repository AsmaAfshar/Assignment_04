# Constant for Mars gravity multiplier
'''MARS_MULTIPLE = 0.378

def main():
    # Step 1: Get the user's Earth weight as input
    earth_weight_str = input("Enter your weight on Earth (in kg): ")

    # Step 2: Convert the input string to a float
    earth_weight = float(earth_weight_str)

    # Step 3: Calculate the Mars weight
    mars_weight = earth_weight * MARS_MULTIPLE

    # Display the result
    print(f"Your weight on Mars would be {mars_weight:.2f} kg.")

if __name__ == '__main__':
    main() '''


# Define gravity constants for each planet relative to Earth
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 1.06
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.19

# Prompt the user for their weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Prompt the user for the name of a planet
planet = input("Enter a planet: ").capitalize()

# Determine the gravitational constant for the selected planet
if planet == "Mercury":
    gravity_constant = MERCURY_GRAVITY
elif planet == "Venus":
    gravity_constant = VENUS_GRAVITY
elif planet == "Mars":
    gravity_constant = MARS_GRAVITY
elif planet == "Jupiter":
    gravity_constant = JUPITER_GRAVITY
elif planet == "Saturn":
    gravity_constant = SATURN_GRAVITY
elif planet == "Uranus":
    gravity_constant = URANUS_GRAVITY
else:
    gravity_constant = NEPTUNE_GRAVITY  # Default to Neptune

# Calculate the equivalent weight on the selected planet
planetary_weight = earth_weight * gravity_constant
rounded_planetary_weight = round(planetary_weight, 2)

# Print the result
print("The equivalent weight on", planet + ":", str(rounded_planetary_weight), "kg")
