def is_anagram(s1,s2):
    s1=s1.replace("","").lower()
    s2=s2.replace("","").lower()

    if len(s1) != len(s2):
        return False
    
    sorted_s1=sorted(s1)
    sorted_s2=sorted(s2)

    return sorted_s1==sorted_s2

string1='listen'
string2='silent'
if is_anagram(string1,string2):
    print(string1,"and",string2,"is a anagrama")
else:
    print(string1,"and",string2,"are not anagrams")    