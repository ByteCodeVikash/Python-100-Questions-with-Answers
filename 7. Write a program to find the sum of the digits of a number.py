num=int(input("Enter a number here: "))

digit_sum=0
while num>0:
    digit=num%10
    digit_sum+=digit
    num//=10
print("the sum of digit number is",digit_sum)    