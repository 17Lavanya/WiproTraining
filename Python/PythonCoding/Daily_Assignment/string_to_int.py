
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"You entered the integer: {number}")
except ValueError:
    print("Error: That was not a valid number.")
