import random

# 1. Generate and print a random integer between 1 and 100
rand_int = random.randint(1, 100)
print(rand_int)

# 2. Create a list of random numbers and print the list
random_list = [random.randint(1, 50) for _ in range(10)]
print(random_list)

# 3. Shuffle a list of numbers and print the shuffled list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)
