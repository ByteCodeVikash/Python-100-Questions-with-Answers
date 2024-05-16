my_list=[1,2,3,4,5,6]

sorted_list=sorted(my_list)

n=len(sorted_list)

if n%2==1:
    median=sorted_list[n//2]

else:
    median=(sorted_list[n//2-1]+sorted_list[n//2])/2


print("median of the given list",median)    
