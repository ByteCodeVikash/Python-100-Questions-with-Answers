def jaccard_similarity(str1,str2):
    set1=set(str1)
    set2=set(str2)

    intersection=set1.intersection(set2)
    union=set1.union(set2)



    jaccard_sim=len(intersection)/len(union)
    return jaccard_sim

str1="hello"
str2="hallo"
print("Jaccard Similarity:",jaccard_similarity(str1,str2))
