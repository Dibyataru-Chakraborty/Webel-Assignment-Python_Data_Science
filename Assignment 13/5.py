def fac(n):
    i=1
    while (n>0):
        i*=n
        n-=1
    return i
n=int(input("Enter the number of elements : "))
print(fac(n))