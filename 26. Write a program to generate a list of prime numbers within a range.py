def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%2==0:
            return False
    return True


def gen_prime_no(strat,end):
    prime=[]

    for num in range(start,end+1):
        if is_prime(num):
            prime.append(num)

    return prime


start=int(input("Enter a strating number here: "))
end=int(input("Enter a end number here: "))

result=gen_prime_no(start,end)

print("prime number in range",start,"to",end,"are",result)