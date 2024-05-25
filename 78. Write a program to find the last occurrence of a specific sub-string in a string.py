main_string="this is my world"
sub_string="my"

last_position=main_string.rfind(sub_string)

if last_position != -1:
    print("the last occurrence sub string ",sub_string,"is found at postion of",last_position,"in main string")
else:
    print(sub_string,"is not found of main string")
