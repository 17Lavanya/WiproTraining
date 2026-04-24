#1. Create a Dictionary
person = {'name': 'ABC','age': 20,'hobby':'Cricket'}
print('Dictionary:',person)

#2. Access name
print('Name:',person['name'])

# 3. Add favorite food,update hobby
person['food']='Biryani'
person['hobby']= 'coding'
print('updated dictionary:',person)

#4.print all keys and Values
print('Keys:',list(person.keys()))
print('Values:',list(person.values()))

#5.Remove age
del person['age']
print('After removing age:',person)