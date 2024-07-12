import re

pwd = input("Enter a password: ")

if not len(pwd) > 5:
    print("Invalid Password")
elif not len(pwd) < 17:
    print("Invalid Password")
elif not re.search('[a-z]', pwd):
    print("Invalid Password")
elif not re.search('[A-Z]', pwd):
    print("Invalid Password")
elif not re.search('[0-9]', pwd):
    print("Invalid Password")
elif not re.search('[#@$]', pwd):
    print("Invalid Password")
else:
    print("Valid Password")

import re
p= input("Input your password: ")
if len(p)>5 and len(p)<17 and re.search('[a-z]',p) and re.search('[A-Z]',p) and re.search('[0-9]',p) and re.search('[$#@_]',p):
    print("valid password")
else:
    print("invalid password")

    import re

text = "xyz@gmil.com and 999@99ad.com and abc_987@vvce.ac.in are the mail ids. (897)-012-3456  ext.23 and 897.012-3456x23 are numbers"
emailRegex = re.compile('[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,4}')
L = emailRegex.findall(text)
for email in L:
    print(email)

    '''
Email id:
    username@domain.type
username : a-z 0-9 . _    ---->     [a-zA-z0-9._]+
@                         ---->     @
domain : a-z 0-9  . -     ---->     [a-zA-z0-9.-]+
.                         ---->     [.]  or \.
type : min 2 to max 4 length    [a-zA-z]{2,4}
'''

import re 
emailRegex = re.compile('''
    [a-zA-Z0-9._]+    # username
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # domain name
    [.]                # dot 
    [a-zA-Z]{2,4}    # type
''', re.VERBOSE)
text = "xyz@gmil.com and 999@99ad.com and abc_987@vvce.ac.in are the mail ids. (897)-012-3456  ext.23 and 897.012-3456x23 are numbers"
L = emailRegex.findall(text)
for email in L:
    print(email)