def copy_file(source, destination):
    try:
        with open(source, "r") as src:
            contents = src.read()


        with open(destination, "w") as dest:
            dest.write(contents)

        print(f"Contents of '{source}' have been copied to '{destination}'.")
    except FileNotFoundError:
        print(f"The file '{source}' was not found.")



copy_file("source.txt", "destination.txt")
