def append_and_read_log(filename, new_line):
    with open(filename, "a") as file:
        file.write(new_line + "\n")

    with open(filename, "r") as file:
        contents = file.read()

    print(f"Contents of '{filename}':")
    print(contents)


append_and_read_log("log.txt", "This is a new log entry.")
