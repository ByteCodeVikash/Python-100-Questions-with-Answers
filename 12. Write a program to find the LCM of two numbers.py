num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))

max_num=max(num1,num2)

Lcm=max_num

while True:
    if Lcm%num1==0 and Lcm%num2==0:
        print("LCM of",num1,"and",num2,"is",Lcm)
        break
    Lcm+=max_num