def find_substrings(s):

    substrings=[]

    for start in range(len(s)):

        for end in range(start+1,len(s)+1):
            substrings.append(s[start:end])
    return substrings


input_string='abc'
substrings=find_substrings(input_string)

print("All sub-strings of the string '{}':".format(input_string))
for substring in substrings:
    print(substring)
