from mypack.circle import areaofcircle, perimeterofcircle
from mypack.basicshapes import areaofsquare,perimeterofsquare,areaofrect

radius = int(input('Enter radius:'))
print('Area: ',areaofcircle(rad= radius))
print('Perimeter: ',perimeterofcircle(rad=radius))


si = int(input('Enter side of square:'))
print('Area: ',areaofsquare(side=si))
print('Perimeter: ',perimeterofsquare(side=si))


l = int(input('enter length:'))
b = int(input('enter breadth:'))
print('Area:',areaofrect(l,b))
