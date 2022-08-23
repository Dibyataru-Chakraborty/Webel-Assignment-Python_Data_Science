#Write a python script to create a list of squares of first N natural numbers. Use for loop to fill list with elements. Value of N is taken from user.
l=[]
n=int(input("Enter the n number: "))
for i in range (1,n+1):
    s=i**2
    l.append(s)
print(l)