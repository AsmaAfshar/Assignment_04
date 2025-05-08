def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Example usage
f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"{f}°F is equal to {c:.2f}°C")