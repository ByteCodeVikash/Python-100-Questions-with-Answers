num=int(input("Enter number here: "))

fact=1

if num<0:
    print("Sorry,factorial does not exit for negative number")
elif num==0:
    print("The factorial o is 1") 
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of",num,"is",fact)           