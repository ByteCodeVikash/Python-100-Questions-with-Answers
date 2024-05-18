def checkvowels(string):
    vowel={'a','e','i','o','u'}

    vowel_count=0

    for char in string:
        if char in vowel:
            vowel_count+=1

    return vowel_count

string=input("Enter a string here: ")

print("Number of vowel in this string",checkvowels(string))