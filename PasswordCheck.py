import re

# Define function to evaluate password strength
def check_password_strength(password):
    ChecksPassed = 0  # Initialize Check score
    
    # 1st Check Check length criteria
    if len(password) >= 8:
        ChecksPassed += 1
    else:
        print("Password should be at least 8 characters long.")
        print("This Password Has failed the check 1")
    
    # 2nd Check  if there are lower case letters
    if re.search(r"[a-z]", password):
        ChecksPassed += 1
    else:
        print("Password does not include lower case letters")
        print("This Password Has failed the check 2")

    # 3rd Check  if there are Upper case letters
    if re.search(r"[A-Z]", password):
        ChecksPassed += 1
    else:
        print("Password does not include upper case letters")
        print("This Password Has failed the check 3")    

    # 4th Check  if there are numbers
    if re.search(r"[0-9]", password):
        ChecksPassed += 1
    else:
        print("Password does not include numbers")
        print("This Password Has failed the check 4") 


    # 5th Check  if there are special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        ChecksPassed += 1
    else:
        print("Password does not include special characters")
        print("This Password Has failed the check 5") 


    # 6th Check for common patterns
    # This can be continious entries like names, dates or common words and number combinations 
    common_patterns = ["1234", "password", "abc", "qwerty"]
    if any(pattern in password for pattern in common_patterns):
        print("Password contains a common pattern. Try something more unique.")
    else:
        ChecksPassed += 1

    # 7th Check for dates
    date_patterns = [
        r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",   # dd-mm-yyyy or dd/mm/yyyy
        r"\b\d{4}[/-]\d{2}[/-]\d{2}\b",   # yyyy-mm-dd or yyyy/mm/dd
        r"\b\d{8}\b",                     # yyyymmdd or ddmmyyyy
        r"\b\d{4}\b",                     # just a year
        r"\d{2}[/-]\d{2}\b"               # dd-mm or dd/mm               
    ]

    if any(re.search(pattern, password) for pattern in date_patterns):
        print("Password contains a date pattern. Try something more unique.")
    else:
        ChecksPassed += 1

    # Output results
    if ChecksPassed >= 5:
        print("Password strength: Strong")
    elif  ChecksPassed < 5:
        print("Password strength: Moderate")
    else:
        print("Password strength: Weak")

# Get user input
password = input("Enter a password to check: ")
check_password_strength(password)
