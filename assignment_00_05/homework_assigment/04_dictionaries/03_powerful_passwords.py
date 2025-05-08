from hashlib import sha256

def hash_password(password):
    """
    Hashes a password using SHA256 and returns the hexadecimal digest.
    """
    return sha256(password.encode()).hexdigest()

def verify_login(email, password, login_data):
    """
    Verifies if the provided email and password match the stored hashed password.

    Parameters:
        email (str): The user's email.
        password (str): The password to verify.
        login_data (dict): Dictionary mapping emails to hashed passwords.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    hashed = hash_password(password)
    stored_hash = login_data.get(email)

    if stored_hash and stored_hash == hashed:
        return True
    return False

def main():
    # Example login database with hashed passwords
    login_database = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("password")
    }

    # Test cases
    test_cases = [
        ("example@gmail.com", "word"),
        ("example@gmail.com", "password"),
        ("code_in_placer@cip.org", "Karel"),
        ("code_in_placer@cip.org", "karel"),
        ("student@stanford.edu", "password"),
        ("student@stanford.edu", "123!456?789"),
        ("nonexistent@email.com", "whatever")
    ]

    for email, pwd in test_cases:
        result = verify_login(email, pwd, login_database)
        status = "✅ Success" if result else "❌ Failed"
        print(f"Login attempt for {email}: {status}")

if __name__ == '__main__':
    main()


#2nd method
from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

# There is no need to edit code beyond this point

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))


if __name__ == '__main__':
    main()