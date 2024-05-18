def is_pangram(sentence):
    sentence=sentence.lower()

    alphabet_set=set()

    for char in sentence:
        if char.isalpha():
            alphabet_set.add(char)


    return len(alphabet_set)==26



sentence=input("Enter a sentence: ")

if is_pangram(sentence):
    
    print("the snetence is a pangram")
else:
    print("This is not a pangram")

