import re
# beg & end match
'''txt = input('Enter a text ') # India is my country
bpat = input('Enter beginning pattern ') #India
epat = input('Enter ending pattern ') #country
bpat = '^' + bpat # ^India
epat = epat + '$' # try$
if re.search(pattern=bpat,string=txt) :
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=epat,string=txt) :
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')'''

#digit
'''mbno = input('Enter a text ')
pat = r"[0-9]"
if re.fullmatch(pattern=pat,string=mbno):
    print('Only digits')
else:
    print('Other characters available')
'''

# Username
'''un = input('Enter UN ')
pat = r"[a-z_]{8,}$"
if re.match(pattern=pat,string=un):
    print('Valid')
else:
    print('Invalid')'''

#email
'''Emailid = input('Email ')
# pat = r"^[a-z A-Z 0-9 _] + @[a-z]+\.[a-z]+$"
if re.match(pattern=pat,string=Emailid):
    print('Valid')
else:
    print('Invalid')'''


#pwd
'''pwdtxt = input('pwd: ')
#pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=[0-9])(?=.*[@ _-]){8,}"
if re.match(pattern=pat,string=pwdtxt):
    print('Valid')
else:
    print('Invalid')'''

txt = input('Text ')
pat = r"\s"
# print(re.sub(pattern=pat,string=txt,repl=' '))
print(re.split(pattern=pat,string=txt))