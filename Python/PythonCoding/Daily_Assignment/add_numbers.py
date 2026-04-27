def add_numbers(a, b):
    try:
        result = a + b
        print(f"The sum is: {result}")
    except TypeError:
        print("Error: Both arguments must be numbers.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    add_numbers(num1, num2)
except ValueError:
    print("Error: Please enter valid numeric values.")
