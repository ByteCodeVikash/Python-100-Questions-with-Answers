def remove_specific_char(s,chars_to_remove):

    translation_table=str.maketrans('','',chars_to_remove)

    return s.translate(translation_table)

input_string="hello ,world! this is a test."

chars_to_remove=",!."

result=remove_specific_char(input_string,chars_to_remove)
print("original string: ",input_string)

print("string after removing specific char: ",result)