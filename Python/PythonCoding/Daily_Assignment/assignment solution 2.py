# count how many times 'a' appeared in a string using enumerate
'''text = 'abracadabraaaabracadab'
count = 0
for index,char in enumerate(text):
    if char == 'a':
        count+= 1
print('count of a:',count)'''

# user input
text = input('Enter a String')
count = 0
for index,char in enumerate(text):
    if char == 'a':
        count+=1
print('count of a:',count)

