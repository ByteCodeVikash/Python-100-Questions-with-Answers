def is_digit(d):
    return d.isdigit()


digits=["1","2","3","4","5"]

for digit in digits:
    print(digit,"is contain only digit",is_digit(digit))