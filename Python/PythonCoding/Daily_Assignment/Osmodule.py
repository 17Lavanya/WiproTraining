import os

# 1. Print the current working directory
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# 2. Create a new directory and verify its existence
new_dir = "test_directory"
os.makedirs(new_dir, exist_ok=True)   # creates the directory if it doesn't exist
print("Directory created:", os.path.exists(new_dir))

# 3. List all files and directories in the current directory
items = os.listdir(current_dir)
print("Files and directories in current directory:")
for item in items:
    print(item)
