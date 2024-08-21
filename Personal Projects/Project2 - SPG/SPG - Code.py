import secrets
import string
import random
import tkinter as tk
from tkinter import messagebox, filedialog

# Generate a random password
def generate_password(length=5):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length * 4))
    return ''.join(random.sample(password, len(password)))

# Add the generated password entry to the list and display it
def add_entry():
    name, login = entry_name.get(), entry_login.get()
    if not name or not login:
        return messagebox.showwarning("Input Error", "Please enter both Name and Login.")
    
    password = generate_password()
    password_entries.append((name, login, password))
    
    # Update the display area
    display_area.insert(tk.END, f"Name: {name}\nLogin: {login}\nPassword: {password}\n{'-'*35}\n")
    entry_name.delete(0, tk.END)
    entry_login.delete(0, tk.END)

# Save all the password entries to a file
def save_entries():
    if not password_entries:
        return messagebox.showwarning("No Entries", "There are no entries to save.")
    
    file_path = filedialog.asksaveasfilename(initialfile="Passwords.txt", defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path: return

    with open(file_path, 'w') as f:
        for name, login, password in password_entries:
            f.write(f"Name: {name}\nLogin: {login}\nPassword: {password}\n{'-'*35}\n")

    messagebox.showinfo("Save Successful", f"Entries have been saved to '{file_path}'")

# Initialise the main application window
app = tk.Tk()
app.title("Secure Pass Generator")
password_entries = []

# User input and display widgets
tk.Label(app, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(app, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app, text="Login:").grid(row=1, column=0, padx=5, pady=5)
entry_login = tk.Entry(app, width=30)
entry_login.grid(row=1, column=1, padx=5, pady=5)

tk.Button(app, text="Generate and Add Entry", command=add_entry).grid(row=2, columnspan=2, pady=10)
display_area = tk.Text(app, height=15, width=50, wrap="word")
display_area.grid(row=3, columnspan=2, pady=10)

tk.Button(app, text="Save Entries", command=save_entries).grid(row=4, columnspan=2, pady=10)

# Start the GUI event loop
app.mainloop()
