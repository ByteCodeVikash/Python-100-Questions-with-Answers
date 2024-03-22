number=int(input("Enter a number here: "))

revers=0

while number>0:
    digit=number%10
    revers=revers*10+digit
    number//=10
print("The reverse of the number is ",revers)    