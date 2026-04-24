# 1.create a list with 5 fruits
fruits =['Apple','Banana','Mango','Grapes','Orange']
print('Original list:',fruits)

# 2. Add two fruits,remove one
fruits.append('Pineapple')
fruits.append('Watermelon')
fruits.remove('Banana')
print('Updated list:',fruits)

# 3.Access second and fourth fruits
print('Second fruit:',fruits[1])
print('Fourth fruit:',fruits[3])

# 4.Slice first three fruits
print('First three fruits:',fruits[:3])

#5. Length of list
print('Length:',len(fruits))