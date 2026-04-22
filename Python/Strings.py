Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s1 = 'hello
SyntaxError: unterminated string literal (detected at line 1)
>>> s1 = 'hello'
>>> s1
'hello'
>>> type(s1)
<class 'str'>
>>> s1.capitalize()
'Hello'
>>> s1.upper()
'HELLO'
>>> s1.lower()
'hello'
>>> s1='hEllO'
>>> s1.casefold()
'hello'
>>> s1='HeLL0'
>>> s1.casefold()
'hell0'
>>> s1.count('l)
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> s1.count('l')
...          
0
>>> s1.count('L')
...          
2
s1.count('L')
         
2



S1.ENDS
         
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    S1.ENDS
NameError: name 'S1' is not defined. Did you mean: 's1'?


sq.ends
         
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sq.ends
NameError: name 'sq' is not defined. Did you mean: 's1'?
s1.find('L)
        
SyntaxError: unterminated string literal (detected at line 1)
s1.find('L'))
         
SyntaxError: unmatched ')'
s1.find('L'))s1.find('L')
SyntaxError: unmatched ')'
s1.find('L')
2








s1.index('o')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s1.index('o')
ValueError: substring not found
s1.insex('h')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s1.insex('h')
AttributeError: 'str' object has no attribute 'insex'. Did you mean: 'index'?
s1.insex('l')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s1.insex('l')
AttributeError: 'str' object has no attribute 'insex'. Did you mean: 'index'?
s1.index('h')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s1.index('h')
ValueError: substring not found
s1
'HeLL0'
s1.index('H')
0
s1.istitle()
False
s1.isalpha()
False
s1
'HeLL0'
s1.isdigit()
False
s1.join(' there')
' HeLL0tHeLL0hHeLL0eHeLL0rHeLL0e'
s1.replace('L','l')
'Hell0'
s1
'HeLL0'
s1='Hello there how are you'
s1
'Hello there how are you'
s1.split(' ')
['Hello', 'there', 'how', 'are', 'you']
s1='Hello there - how are you'
s1.split('-')
['Hello there ', ' how are you']

================ RESTART: C:/Wipro Training/Python/str1ex.py ================
*-*-*-*-*-*-*-*-*-*-*-*-*-*-

================ RESTART: C:/Wipro Training/Python/str1ex.py ================
h
e
l
l
o
 
t
h
e
r
e
!
!
!

================ RESTART: C:/Wipro Training/Python/str1ex.py ================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!

================ RESTART: C:/Wipro Training/Python/str1ex.py ================
h
e
l
l
o

================ RESTART: C:/Wipro Training/Python/str1ex.py ================
h
e
l
l
o
