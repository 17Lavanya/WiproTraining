
numbers = [10, 20, 30, 40, 50]
index_str = input("Enter an index to access an element (0-4): ")

try:
    index = int(index_str)
    element = numbers[index]
    print(f"Element at index {index}: {element}")

except ValueError:
    print("Error: Please enter a valid integer index.")

except IndexError:
    print("Error: Index out of range. Valid indices are 0 to", len(numbers) - 1)
