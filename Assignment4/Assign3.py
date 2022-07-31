#write a python script to print  1st n prime number. Value of n is given by user.
n = int(input("Enter the number: "))
print ("The 1st n Prime Numbers in the range are: ")  
for i in range(1,n+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")