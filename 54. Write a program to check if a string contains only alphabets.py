def is_alpha(s):
    return s.isalpha()

strings=["hello","hello123","123"]

for string in strings:
    print(string,"contain only alpha",is_alpha(string))