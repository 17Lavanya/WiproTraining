#1.Create a set of 5 colors
colors ={'Red','Blue','Green','Yellow','Purple'}
print('colors set:',colors)

#2. Add and remove a color
colors.add('Pink')
colors.remove('Yellow')
print('Updated set:',colors)

# 3.Intersection,Union,Difference
colors2={'Red','Black','White'}
print('Intersection:',colors & colors2)
print('Union:',colors | colors2)
print('Difference:',colors-colors2)

#4.Check if color exists
print('Is "Red" in set?',"Red" in colors)

#5.Convert list with duplicates to set
fruit_list =['Apple','Mango','Apple','Banana','Mango']
unique_fruits = set(fruit_list)
print('Unique fruits:',unique_fruits)