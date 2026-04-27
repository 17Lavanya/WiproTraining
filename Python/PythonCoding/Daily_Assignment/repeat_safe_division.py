while True:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    try:
        num1 = int(num1_str)
        num2 = int(num2_str)

        result = num1 / num2
        print(f"Result of division: {result}")
        break

    except ValueError:
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Try again.")
