grade = input('Enter grade').upper()
match grade:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')
    case 'C':
        print('Average')
    case 'D':
        print('Below Average')
    case _:
        print('Invalid')