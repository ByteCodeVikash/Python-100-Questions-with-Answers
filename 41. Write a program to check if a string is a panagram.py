import string

def is_panagram(s):
    s=s.lower()

    alphabet_set=set(string.ascii_lowercase)

    s_set=set(s)

    return alphabet_set.issubset(s_set)

input_string="the quick brown fox jumps over the lazy dog"

result=is_panagram(input_string)

if result:
    print("this is a panagram")
else:
    print("this is not panagra")