import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PasswordCheck import check_password_strength
from PasswordGenerator import generate_strong_password

# Function to handle button click and show password strength
def evaluate_password():
    password = entry.get()  # Get password from input field
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# Function to generate a strong password and display it
def generate_password():
    password = generate_strong_password(12)  # Adjust the length as needed
    entry.delete(0, tk.END)  # Clear any existing text in the entry field
    entry.insert(0, password)  # Insert the generated password
    generated_password_label.config(text=f"Generated Password: {password}")  # Display the generated password

# Best Practices for Password Creation
best_practices_text = """
Best Practices for Password Creation:
- Use at least 8 characters.
- Include a mix of uppercase and lowercase letters.
- Add numbers and special characters.
- Avoid common patterns and repeated sequences.
- Do not include personal information (e.g., dates).
"""

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")  # Initial window size
root.configure(bg="#f5f5f5")  # Background color
root.resizable(True, True)  # Allow window resizing

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10), background="#f5f5f5")
style.configure("TButton", font=("Helvetica", 10, "bold"), background="#007ACC", foreground="Black")

# Header Label
header_label = ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

# Instruction Label
label = ttk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Password entry field
entry = ttk.Entry(root, show="*", width=30, font=("Helvetica", 10))
entry.pack(pady=10)

# Button to check password strength
button_check = ttk.Button(root, text="Check Strength", command=evaluate_password)
button_check.pack(pady=5)

# Button to generate a strong password
button_generate = ttk.Button(root, text="Generate Strong Password", command=generate_password)
button_generate.pack(pady=5)

# Label to display the generated password
generated_password_label = ttk.Label(root, text="", font=("Helvetica", 10, "bold"), foreground="#007ACC")
generated_password_label.pack(pady=5)

# Frame for Best Practices
best_practices_frame = ttk.LabelFrame(root, text="Password Creation Best Practices", padding=(10, 10))
best_practices_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Best Practices Text
best_practices_label = ttk.Label(best_practices_frame, text=best_practices_text, font=("Helvetica", 9), wraplength=350)
best_practices_label.pack()

# Run the GUI loop
root.mainloop()
