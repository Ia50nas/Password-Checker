import re

def check_password_strength(password):
    checks_passed = 0  # Initialize check score
    feedback = []  # To collect feedback messages

    # 1st Check: Check length criteria
    if len(password) >= 8:
        checks_passed += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # 2nd Check: Check for lowercase letters
    if re.search(r"[a-z]", password):
        checks_passed += 1
    else:
        feedback.append("Password does not include lowercase letters.")
    
    # 3rd Check: Check for uppercase letters
    if re.search(r"[A-Z]", password):
        checks_passed += 1
    else:
        feedback.append("Password does not include uppercase letters.")
    
    # 4th Check: Check for numbers
    if re.search(r"[0-9]", password):
        checks_passed += 1
    else:
        feedback.append("Password does not include numbers.")
    
    # 5th Check: Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        checks_passed += 1
    else:
        feedback.append("Password does not include special characters.")
    
    # 6th Check: Check for common patterns
    common_patterns = ["1234", "password", "abc", "qwerty"]
    if any(pattern in password for pattern in common_patterns):
        feedback.append("Password contains a common pattern. Try something more unique.")
    else:
        checks_passed += 1
    
    # 7th Check: Check for dates
    date_patterns = [
        r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",   # dd-mm-yyyy or dd/mm/yyyy
        r"\b\d{4}[/-]\d{2}[/-]\d{2}\b",   # yyyy-mm-dd or yyyy/mm/dd
        r"\b\d{8}\b",                     # yyyymmdd or ddmmyyyy
        r"\b\d{4}\b",                     # just a year
        r"\d{2}[/-]\d{2}\b"               # dd-mm or dd/mm
    ]
    
    if any(re.search(pattern, password) for pattern in date_patterns):
        feedback.append("Password contains a date pattern. Try something more unique.")
    else:
        checks_passed += 1
    
        # 8th Check: Repetition Detection
    if re.search(r"(.)\1{2,}", password):  # Detects sequences with 3 or more repeated characters
        feedback.append("Password contains repeating sequences. Try to make it more varied.")
    else:
        checks_passed += 1
    
    # 9th Check: Complexity Evaluation (Balanced use of characters)
    if re.search(r"^[A-Za-z]+$", password) or re.search(r"^[0-9]+$", password):
        feedback.append("Password is unbalanced; avoid long stretches of only letters or only numbers.")
    else:
        checks_passed += 1

    # Determine password strength based on total points
    if checks_passed >= 7:
        strength = "Strong"
    elif 5 <= checks_passed < 7:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    feedback.append(f"Password strength: {strength}")
    return "\n".join(feedback)
