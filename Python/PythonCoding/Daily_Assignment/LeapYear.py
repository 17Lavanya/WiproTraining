Year = int(input('Enter a year:'))
if(Year %4== 0 and Year %100 == 0 ) or Year %400 == 0:
    print('Leap year.')
else:
    print('Not a leap year')