# Password Strength Checker

The Password Strength Checker Application is a simple, user-friendly tool designed to help users evaluate the security strength of their passwords. This application provides instant feedback on key password criteria, guiding users to create stronger, more secure passwords that meet modern security standards.

## How It Works

The Password Strength Checker evaluates passwords based on several key security checks to ensure complexity and uniqueness. Based on reseach bad password creation has some specific predictable patterns. Each check is designed to encourage a higher level of security by identifying potential weaknesses in the password structure.

### Security Checks

1. **Length Requirement**  
   - **Check**: Password must be at least 8 characters long.  
   - **Reason**: Longer passwords are harder to crack and add a strong layer of security.

2. **Lowercase Letters**  
   - **Check**: Password must include at least one lowercase letter (`a-z`).  
   - **Reason**: Mixing character types (lowercase and uppercase) increases complexity.

3. **Uppercase Letters**  
   - **Check**: Password must contain at least one uppercase letter (`A-Z`).  
   - **Reason**: A combination of uppercase and lowercase letters makes passwords more challenging to guess.

4. **Numbers**  
   - **Check**: Password must contain at least one numeric digit (`0-9`).  
   - **Reason**: Adding numbers introduces complexity, strengthening the password against brute-force attacks.

5. **Special Characters**  
   - **Check**: Password must include at least one special character (e.g., `!@#$%^&*`).  
   - **Reason**: Special characters make the password less predictable and harder to guess.

6. **Common Patterns**  
   - **Check**: Identifies common, easily guessed patterns, such as `"1234"`, `"password"`, `"abc"`, or `"qwerty"`.  
   - **Reason**: Predictable patterns are often targeted by attackers, so avoiding them increases security.

7. **Date Patterns**  
   - **Check**: Detects date patterns in various formats (e.g., `dd-mm-yyyy`, `mm-dd-yyyy`, `yyyymmdd`, or a standalone year).  
   - **Reason**: Dates, especially birthdates, are often used and easily guessed, so this check encourages users to avoid date-related patterns.
