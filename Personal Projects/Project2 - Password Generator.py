#!/usr/bin/env python
# coding: utf-8

# # Password Generator

# In[20]:


# Generate a password that has exactly 3 of each type of character
# (e.g. 3 random lowercase letters, 3 random digits, 3 random special characters, etc.)

import secrets
import string
import random

# Number of each type of character
count = 3

# Generate 3 random uppercase letters
upper_case = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(count))

# Generate 3 random lowercase letters
lower_case = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(count))

# Generate 3 random digits
digits = ''.join(secrets.choice(string.digits) for _ in range(count))

# Generate 3 random special characters
special_characters = ''.join(secrets.choice(string.punctuation) for _ in range(count))

# Combine all parts into one password
password = upper_case + lower_case + digits + special_characters

# Shuffle the password to ensure randomness
password = ''.join(random.sample(password, len(password)))

# Print the result
print("Your generated random password: " + password)


# In[ ]:




