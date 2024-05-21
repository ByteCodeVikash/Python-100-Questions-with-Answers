def is_palinfrom(s):
    s=s.lower()

    s=''.join(char for char in s if char.isalnum())

    return s==s[::-1]

input_string="A man, a plan,a canal,panama"

result=is_palinfrom(input_string)

if result:
    print("this is palindrome")
else:
    print("this is not palindrom")    