def sum(n):
    temp=n
    sum=0
    print("Sum of the digites is : ")
    while(n>0):
        rim=n%10
        sum+=rim
        n//=10
    return sum
n=int(input("Enter the number of elements : "))
print(sum(n))