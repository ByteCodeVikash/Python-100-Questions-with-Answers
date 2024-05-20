def most_common_char(string):
    max_count=0
    max_common_char=''
    for char in string:
        count=0
        for c in string:
            if c==char:
                count+=1

        if count>max_count:
            max_count=count
            most_common_char=char
    return most_common_char            

input_string=input("Enter a string: ")
most_common=most_common_char(input_string) 
print("The most common character in the string is: ",most_common)           
