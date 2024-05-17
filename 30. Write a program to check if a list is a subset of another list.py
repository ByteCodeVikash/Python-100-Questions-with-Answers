def subset(l1,l2):
    if set(l1).issubset(set(l2)):
        print("l1 is sub set l2")
    else:
        print("l1 is not subset l2")

l1=[1,2,3,4]
l2=[1,2,3,4]

subset(l1,l2)