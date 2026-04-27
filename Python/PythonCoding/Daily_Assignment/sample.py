def count_file_contents(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            line_count = text.count("\n") + (1 if text else 0)
            word_count = len(text.split())
            char_count = len(text)

            print(f"File: {filename}")
            print(f"Lines: {line_count}")
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")



count_file_contents("sample.txt")
