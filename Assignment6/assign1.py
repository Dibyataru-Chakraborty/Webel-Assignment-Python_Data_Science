#Write a python script to sort a list given by user
l=[]
n=int(input("Enter the number of element: "))
for i in range(0,n):
    m=int(input())
    l.append(m)
    l.sort()
print(l)