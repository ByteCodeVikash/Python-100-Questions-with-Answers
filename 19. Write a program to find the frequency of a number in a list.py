

l1=[1,2,3,3,4,5]

frq={}
for i in l1:
    if i in frq:
        frq[i]+=1
    else:
        frq[i]=1    

print(frq)