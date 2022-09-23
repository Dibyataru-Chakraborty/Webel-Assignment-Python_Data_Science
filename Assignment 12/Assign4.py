def natural(n):
    print("The first ",n," even natural numbers are :")
    i,c=1,1
    while(c<=n):
        if(i%2==1):
            print(i,end=" ")
            c+=1
        i+=1
n=int(input("Enter the last range : "))
natural(n)