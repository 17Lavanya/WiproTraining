
class NegativeNumberError(Exception):
    """Raised when the input number is negative."""
    pass

user_input = input("Enter a positive number: ")

try:
    number = int(user_input)

    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print(f"You entered a valid positive number: {number}")

except ValueError:
    print("Error: Please enter a valid integer.")

except NegativeNumberError as e:
    print(f"Error: {e}")
