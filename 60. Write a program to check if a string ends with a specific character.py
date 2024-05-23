def is_end(h,char):
    return h.endswith(char)

string=['viaksh','shivam','jalaj']
specific_char='h'

for i in string:
    print(i,"is contain",is_end(i,specific_char))