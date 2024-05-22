import re

def is_valideamil(email):

    email_regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


    if re.match(email_regex,email):
        return True
    else:
        return False
    
emails=["test@email.com","Invalid-email","another-domain@test.com","bod@domain@email.com"] 


for email in emails:
    print(email,"is a valid",is_valideamil(email))