def is_lower(l):
    return l.islower()

lower=['abc','Abc','abC']

for low in lower:
    print(low,"is conatin only",is_lower(low))