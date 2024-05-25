def word_freq(s):

    s=s.lower()

    import string

    s=s.translate(str.maketrans('','',string.punctuation))

    words=s.split()

    frequency={}

    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1

    return frequency


test_string="hello,world! eveyone.this is a test"
frequencies=word_freq(test_string)

for word,count in frequencies.items():
    print(word,count)