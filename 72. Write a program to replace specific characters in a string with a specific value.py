def replace_specific_chars(s,chars_to_replace,replacement):
    for char in chars_to_replace:
        s=s.replace(char,replacement)
    return s

input_string="hello,world! this is a test."

chars_to_replace=",!."
replacement="*"

result=replace_specific_chars(input_string,chars_to_replace,replacement)

print("original string",input_string)
print("string after replacing specific char:",result)