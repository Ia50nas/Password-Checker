import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PasswordCheck import check_password_strength
from PasswordGenerator import generate_strong_password

# Function to evaluate password strength and update strength label with color coding
def evaluate_password():
    password = entry.get()  # Get password from input field
    result = check_password_strength(password)
    
    # Separate strength from feedback messages
    feedback_lines = result.split("\n")
    strength = feedback_lines[-1]  # Last line is the strength message
    feedback_messages = "\n".join(feedback_lines[:-1])  # All lines except the last are feedback
    
    # Update the strength label based on the strength result
    if "Strong" in strength:
        strength_label.config(text="Strong", foreground="green")
    elif "Moderate" in strength:
        strength_label.config(text="Moderate", foreground="orange")
    else:
        strength_label.config(text="Weak", foreground="red")
    
    # Display feedback messages in the comments label
    comments_label.config(text=feedback_messages)

# Function to generate a strong password and display it
def generate_password():
    length = length_scale.get()  # Get the desired length from the slider
    password = generate_strong_password(length)  # Generate password with specified length
    
    # Check the "Show Password" box and set password visibility to plain text
    show_password_var.set(True)  # Set the checkbox to checked
    entry.config(show="")  # Show password in plain text
    
    entry.delete(0, tk.END)  # Clear any existing text in the entry field
    entry.insert(0, password)  # Insert the generated password
    generated_password_label.config(text="Generated Password displayed above")  # Update the info label
    
    # Set strength label to "Strong" when a password is generated
    strength_label.config(text="Strong", foreground="green")
    comments_label.config(text="")  # Clear comments when a new password is generated

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x700")  # Adjusted window size to fit additional information
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

# Password Strength Label
strength_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold"))
strength_label.pack(pady=5)

# Comments Label to display detailed feedback on the current password
comments_label = ttk.Label(root, text="", font=("Helvetica", 10), wraplength=350, justify="left")
comments_label.pack(pady=5)

# Checkbox to show or hide password
show_password_var = tk.BooleanVar()
show_password_check = ttk.Checkbutton(
    root,
    text="Show Password",
    variable=show_password_var,
    command=lambda: entry.config(show="" if show_password_var.get() else "*")
)
show_password_check.pack(pady=5)

# Button to check password strength
button_check = ttk.Button(root, text="Check Strength", command=evaluate_password)
button_check.pack(pady=5)

# Button to generate a strong password
button_generate = ttk.Button(root, text="Generate Strong Password", command=generate_password)
button_generate.pack(pady=5)

# Label to display the generated password message
generated_password_label = ttk.Label(root, text="", font=("Helvetica", 10, "bold"), foreground="#007ACC")
generated_password_label.pack(pady=5)

# Customizable Password Length Slider
length_label = ttk.Label(root, text="Select Random Generated Password Length:")
length_label.pack(pady=5)
length_scale = tk.Scale(root, from_=8, to=20, orient="horizontal")
length_scale.set(12)  # Default length
length_scale.pack(pady=5)

# Frame for Strong Password Guidelines
guidelines_frame = ttk.LabelFrame(root, text="Tips for a Strong Password", padding=(10, 10))
guidelines_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Guidelines Text
guidelines_text = """
A strong password should:
- Be at least 8 characters long
- Include a mix of uppercase and lowercase letters
- Contain numbers and special characters (e.g., @, #, $)
- Avoid common words or sequences (e.g., "password", "1234")
- Do not contain dates like birthday
"""

# Label to display the guidelines
guidelines_label = ttk.Label(guidelines_frame, text=guidelines_text, font=("Helvetica", 9), wraplength=350, justify="left")
guidelines_label.pack()

# Run the GUI loop
root.mainloop()
