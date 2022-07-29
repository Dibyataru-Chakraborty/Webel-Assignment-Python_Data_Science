#Write a python script to calculate product of first n odd natural number. Number is taken from user
n=int(input("Enter the number: "))
pro=1
for i in range(1,n+1):
    if i%2!=0:
        pro*=i
print("The product of first n odd natural number: ",pro)