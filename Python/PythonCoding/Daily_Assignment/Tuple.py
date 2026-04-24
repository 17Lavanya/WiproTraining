#1.Create a tuple with 3 cities
cities = ('Paris','Tokyo','London')
print('cities tuple:',cities)

# 2.First and last elements
print('First city:',cities[0])
print('Last city:',cities[-1])

# 3.Concatenate two tuples
more_cities=('Dubai','New York')
all_cities = cities+more_cities
print('Combined tuple:',all_cities)

# 4. Try changing an element
try:
    cities[0] = 'Berlin'
except TypeError as e:
    print('Error:',e)

# 5. Unpack tuple
c1,c2,c3,c4,c5 = all_cities
print('Unpacked:',c1,c2,c3,c4,c5)
