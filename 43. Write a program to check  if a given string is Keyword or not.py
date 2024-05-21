import keyword

def iskeyword(word):
    keyword_list=keyword.kwlist

    if word in keyword_list:
        return "Yes"
    else:
        return "No"
    
if __name__=="__main__":
    print(iskeyword("geeks"))
    print(iskeyword("for"))    