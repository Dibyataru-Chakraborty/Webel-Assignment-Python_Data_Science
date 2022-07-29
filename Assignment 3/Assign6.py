#Write a python a script to print first N natural numbers in reverse order. Value is taken from user.
n=int(input("Enter the number: "))
for i in range (n,-1,-1):
    print(i,end=" ")