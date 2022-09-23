def natural(n):
    print("The first ",n," even natural number's sum is :")
    i,c,s=1,1,0
    while(c<=n):
        if(i%2==0):
            s+=i
            c+=1
        i+=1
    return s
n=int(input("Enter the number of elements : "))
print(natural(n))