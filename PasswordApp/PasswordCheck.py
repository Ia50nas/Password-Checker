import re

def check_password_strength(password):
    ChecksPassed = 0  # Initialize Check score
    feedback = []  # To collect feedback messages

    # 1st Check: Check length criteria
    if len(password) >= 8:
        ChecksPassed += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        ChecksPassed -= 2
    
    # 2nd Check: Check for lowercase letters
    if re.search(r"[a-z]", password):
        ChecksPassed += 1
    else:
        feedback.append("Password does not include lowercase letters.")
    
    # 3rd Check: Check for uppercase letters
    if re.search(r"[A-Z]", password):
        ChecksPassed += 1
    else:
        feedback.append("Password does not include uppercase letters.")
    
    # 4th Check: Check for numbers
    if re.search(r"[0-9]", password):
        ChecksPassed += 1
    else:
        feedback.append("Password does not include numbers.")
    
    # 5th Check: Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        ChecksPassed += 1
    else:
        feedback.append("Password does not include special characters.")
    
    # 6th Check: Check for common patterns
    common_patterns = ["1234", "password", "abc", "qwerty"]
    if any(pattern in password for pattern in common_patterns):
        feedback.append("Password contains a common pattern. Try something more unique.")
        ChecksPassed -= 2
    else:
        ChecksPassed += 1
    
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
        ChecksPassed += 1
    
    # Determine password strength
    if ChecksPassed >= 5:
        strength = "Strong"
    elif ChecksPassed == 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    feedback.append(f"Password strength: {strength}")
    return "\n".join(feedback)
