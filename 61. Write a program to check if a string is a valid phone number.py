import re

def is_validno(phone):

    regex_no=r'^\d{10}$'

    if re.match(regex_no,phone):
        return True
    else:
        return False
    

string=['12345677','1234567890','7618040212']

for i in string:
    print(i,"is a valid ",is_validno(i))
    