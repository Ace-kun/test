def fact(n):
    fac =1
    for i in range(1,n+1):
        fac*=i
    return fac

n = int(input("Enter ur Number: "))
print(fact(n))
