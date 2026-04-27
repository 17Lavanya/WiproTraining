filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print(f"Contents of '{filename}':")
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

finally:
    print("Program has completed execution.")
