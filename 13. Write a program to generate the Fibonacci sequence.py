
n=int(input("Enter a number generate fib: "))

a,b=0,1
count=0

if n<0:
    print("Enter a postitve numher here: ")
elif n==1:
    print("fibonacci series",n,":",a)
else:
    print("Febonacci series")
    while count<n:
        print(a,end='')
        nth=a+b 
        a=b
        b=nth
        count+=1   