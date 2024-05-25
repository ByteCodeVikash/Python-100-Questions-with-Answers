def remove_leading_trailing_whitespaces(s):
    return s.strip()

input_string="    hello , world    "
result=remove_leading_trailing_whitespaces(input_string)

print("original string",input_string)
print("string after removing leading and trailing whitespaces: ",result)