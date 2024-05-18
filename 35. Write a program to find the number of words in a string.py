def find_no_of_word(string):
    word=1

    for i in string:
        if i == ' ':
            word+=1
    return word

string=input("Enter a string here: ")

print("the number of word is",find_no_of_word(string))