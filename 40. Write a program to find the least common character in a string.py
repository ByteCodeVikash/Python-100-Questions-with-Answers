from collections import Counter

def least_common_char(string):

    char_count=Counter(string)

    least_commom=min(char_count,key=char_count.get)

    return least_commom

input_string="Hello world"


result=least_common_char(input_string)

print(result)
