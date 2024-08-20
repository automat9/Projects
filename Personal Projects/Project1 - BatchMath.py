#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Pre-defined list of operations
operations = ["multiply", "divide", "add", "subtract"]

# Map operations to their respective symbols
operation_symbols = {
    "multiply": "*",
    "divide": "/",
    "add": "+",
    "subtract": "-"
}

while True:
    # Ask the user to choose an operation
    choice = input("Choose an operation: multiply, divide, add, subtract: ").lower()

    if choice in operations:
        print(f"You chose to {choice}.")
        break
    else:
        print("Invalid choice. Please select a valid operation.")

x = int(input(f"How many numbers would you like to {choice}: "))
y = float(input(f"Enter the number to {choice} by: "))

result_list = []
symbol = operation_symbols[choice]  # Get the symbol for the chosen operation

for i in range(1, x + 1):
    if choice == "multiply":
        result = i * y
    elif choice == "divide":
        result = i / y
    elif choice == "add":
        result = i + y
    elif choice == "subtract":
        result = i - y
    result_list.append(f"{i} {symbol} {y} = {result}")

# Print the results
for item in result_list:
    print(item)


# In[ ]:




