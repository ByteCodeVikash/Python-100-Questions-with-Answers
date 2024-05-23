import re

def is_validcard(card):

    regex_no = r'^((4\d{12})|(5[1-5]\d{14})|(3[47]\d{13})|(6\d{15})|(6011\d{12}))$'
    if re.match(regex_no,card):
        return True
    else:
        return False
    

string=["4111111111111111", "5500000000000004", "340000000000009", "6011000000000004", "1234567890123456"]

for i in string:
    print(i,"is valid card",is_validcard(i))