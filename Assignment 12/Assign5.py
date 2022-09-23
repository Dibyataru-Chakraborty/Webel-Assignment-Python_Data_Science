def natural(n):
    print("The first ",n," even natural numbers are :")
    l=[]
    i,c=1,1
    while(c<=n):
        if(i%2==1):
            l.append(i)
            c+=1
        i+=1
    l.reverse()
    for i in l:
        print(i,end=' ')
n=int(input("Enter the last range : "))
natural(n)