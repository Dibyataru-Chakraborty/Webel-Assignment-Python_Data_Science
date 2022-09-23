def natural(n):
    s=0
    print("The first ",n," natural number's sum is :")
    for i in range(1,n+1):
        s+=i
    return s
n=int(input("Enter the number of elements : "))
print(natural(n))