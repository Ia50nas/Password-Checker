import tkinter as tk
from tkinter import messagebox
from PasswordCheck import check_password_strength

# Function to handle button click and show password strength
def evaluate_password():
    password = entry.get()  # Get password from input field
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

# Label
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Password entry field
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

# Button to check password strength
button = tk.Button(root, text="Check Strength", command=evaluate_password)
button.pack(pady=20)

# Run the GUI loop
root.mainloop()
