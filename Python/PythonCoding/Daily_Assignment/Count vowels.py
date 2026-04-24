s = input('Enter a string:')
count = 0
for c in s.lower():
    if c in 'aeiou':
        count = count + 1
print('vowel count:',count)