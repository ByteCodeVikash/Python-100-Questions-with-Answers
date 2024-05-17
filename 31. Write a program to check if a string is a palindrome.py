def palindrome(s):
    return s==s[::-1]

s="malayalam"

answer=palindrome(s)

if answer:
    print("yes")
else:
    print("NO")    