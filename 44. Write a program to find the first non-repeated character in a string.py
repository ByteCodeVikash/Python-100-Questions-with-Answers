def first_non_repeated_char(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return s[i]
        return None
    
input_string="swiss"

result=first_non_repeated_char(input_string)

if result:
    print("the first non char in string",result)
else:
    print("there is no non-repeated in the string ",input_string)

