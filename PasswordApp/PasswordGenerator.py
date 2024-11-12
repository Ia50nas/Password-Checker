import random
import string

def generate_strong_password(length=12):
    """Generates a strong password with a specified length.
    
    The password will contain uppercase letters, lowercase letters, numbers, 
    and special characters to ensure high strength.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for strong security.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Ensure the password includes at least one character from each set
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + special_characters
    password_chars += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to avoid any predictable order
    random.shuffle(password_chars)
    
    # Join the list into a string to form the final password
    password = ''.join(password_chars)
    return password
