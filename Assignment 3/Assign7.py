#Write a python script to calculate sum of first N natural numbers. Value of N taken from user.
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first natural number",sum)