#Write a python script to calculate factorial of a number. Number is taken from user
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("The factorial: ",fact)