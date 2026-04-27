import csv
import os

def write_csv(filename):
    data = [
        {'name': 'ABC', 'age': 20},
        {'name': 'XYZ', 'age': 26}
    ]
    columnnames = ["name", "age"]
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")

filename = "myfilename.csv"
write_csv(filename)
print("Data read from csv file:")
read_csv(filename)
