num=int(input("Enter number here: "))

if num<=0:
    print("Please enter a postive numbre ")
elif num==1:
    print("This is not prime numbere")

else:
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    if isprime:
        print("This is prime number")
    else:
        print("This is non-prime number")        
