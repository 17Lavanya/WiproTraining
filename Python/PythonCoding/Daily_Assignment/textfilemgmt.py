user_input = input("Please enter some text: ")
with open("output.txt", "w") as file:
    file.write(user_input)
with open("output.txt", "r") as file:
    contents = file.read()
print("The contents of output.txt are:")
print(contents)
