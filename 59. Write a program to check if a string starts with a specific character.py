def is_start(s,char):
    return s.startswith(char)


string=['jalaj','shivam','vikash']
specific_char='s'

for i in string:
    print(i,"is contain",is_start(i,specific_char))