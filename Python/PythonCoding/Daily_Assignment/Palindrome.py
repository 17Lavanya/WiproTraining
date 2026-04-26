def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

test_strings = ["madam", "Hii", "hello", "level", "Python"]
for word in test_strings:
    result = is_palindrome(word)
    print("Word:", word, "Palindrome:", result)
