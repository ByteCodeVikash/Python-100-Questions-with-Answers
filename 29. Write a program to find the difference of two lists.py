def checklistitem(l1,l2):
    return list(set(l1)-(set(l2)))


l1=[1,2,34,4,66,7]
l2=[1,2,3,34,65,6,7]

print(checklistitem(l1,l2))