from string_utils import string_operations, string_validations

# String operations
text = "HelloWorld"
print("Original:", text)
print("Reversed:", string_operations.reverse_string(text))
print("Uppercase:", string_operations.to_uppercase(text))
print("Length:", string_operations.string_length(text))

# String validations
word1 = "mam"
word2 = "Python"

print(f"Is '{word1}' a palindrome?", string_validations.is_palindrome(word1))
print(f"Does '{word2}' contain only alphabets?", string_validations.is_alpha(word2))
