# Define operations and their symbols
operations = {
    "multiply": "*",
    "divide": "/",
    "add": "+",
    "subtract": "-"
}

while True:
    choice = input("Choose an operation: multiply, divide, add, subtract: ").lower()

    if choice in operations:
        print(f"You chose to {choice}.")
        break
    else:
        print("Invalid choice. Please select a valid operation.")

x = int(input(f"How many numbers would you like to {choice}: "))
y = float(input(f"Enter a number to {choice} by: "))

result_list = []
symbol = operations[choice]

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


