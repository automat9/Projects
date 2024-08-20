# Generates a random string of 20 characters - complementary password manager in progress

import secrets
import string
import random

# How many characters of each type
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

# Print the result
print("Your generated random password:", password)
