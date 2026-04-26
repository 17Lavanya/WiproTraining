#1: Largest and Smallest from a list of numbers ──
numbers = list(map(int, input("Enter numbers : ").split()))
print("Largest number :", max(numbers))
print("Smallest number:", min(numbers))

print()

# 2: Length of a string ──
text = input("Enter a string: ")
print("Length of string:", len(text))

print()

# 3: List of names in alphabetical order ──
names = input("Enter names : ").split()
print("Alphabetical order:", sorted(names))

print()

# 4: Total sum of a list of numbers ──
nums = list(map(int, input("Enter numbers : ").split()))
print("Total sum:", sum(nums))

print()

# 5: String in uppercase ──
phrase = input("Enter a string: ")
print("Uppercase:", phrase.upper())