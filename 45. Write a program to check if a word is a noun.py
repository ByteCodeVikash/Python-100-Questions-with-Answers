import nltk
nltk.download('averaged_perceptron_tagger')


text = 'India'


tokens = nltk.word_tokenize(text)


ans = nltk.pos_tag(tokens)


val = ans[0][1]


if val in ('NN', 'NNS', 'NNPS', 'NNP'):
    print(text, "is a noun")
else:
    print(text, "is not a noun")
   