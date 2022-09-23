def nextprime(n):
    p=n+1
    for i in range(2,p):
        if(p%i==0):
            p=p+1
    else:
       return p
num=int(input("Enter a Number: "))
x=nextprime(num)
print("The Next prime number is: ",x)