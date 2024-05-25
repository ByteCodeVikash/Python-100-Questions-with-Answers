main_string="this is my world"

sub_string="my"

postion=main_string.find(sub_string)

if postion !=-1:
    print("the sub string",sub_string,"is the found at position",postion,"in the main string")
else:
    print("the sub string",sub_string,"is not found in the main string")    