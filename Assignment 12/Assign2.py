def natural(n):
    print("The first ",n," natural numbers in reverse order are :")
    while(n>0):
        print(n,end=" ")
        n-=1
n=int(input("Enter the last range : "))
natural(n)