''''import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to prevent predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))'''


import random
import string
def password_generated(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# user inputs

length = int(input("Enter the length of your desired password: "))

password = password_generated(length)
print("Your Desired Password Generated:" , password)