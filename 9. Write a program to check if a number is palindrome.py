#Palindrome Program in Python using While Loop

n=int(input("Enter a number here: "))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("This is palindrome")
else:
    print("this is not palindrome")  

    
          