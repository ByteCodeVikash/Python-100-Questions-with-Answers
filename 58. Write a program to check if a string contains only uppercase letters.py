def is_upper(u):
    return u.isupper()

upper=['ABC','abc','aBc','abC']

for i in upper:
    print(i,"is contain",is_upper(i))