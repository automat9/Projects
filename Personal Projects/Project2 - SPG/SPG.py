import secrets
import string
import random
import os

# Initialize an empty list to store the password entries
password_entries = []

while True:
    # Ask for the name of the entry
    name = input("Enter the name for this entry: ")

    # Always ask for the login associated with this entry
    login = input("Enter the login: ")

    # How many characters of each type for the password
    count = 5

    # Generate the components of the password
    password = (
        ''.join(secrets.choice(string.ascii_uppercase) for _ in range(count)) +
        ''.join(secrets.choice(string.ascii_lowercase) for _ in range(count)) +
        ''.join(secrets.choice(string.digits) for _ in range(count)) +
        ''.join(secrets.choice(string.punctuation) for _ in range(count))
    )

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    # Inform the user of the generated password
    print("Your generated random password:", password)

    # Store the entry in the list as a tuple
    password_entries.append((name, login, password))

    # Ask if the user wants to generate another password
    another = input("Would you like to generate another entry? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# Get the path to the user's desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the full path for the text file on the desktop
file_path = os.path.join(desktop_path, 'passwords.txt')

# Write the entries to the text file in the specified format
with open(file_path, 'w') as f:
    for name, login, password in password_entries:
        f.write(f"Name: {name}\n")
        f.write(f"Login: {login}\n")
        f.write(f"Password: {password}\n")
        f.write("-----------------------------------\n")

print(f"\nEntries have been saved to '{file_path}'")
