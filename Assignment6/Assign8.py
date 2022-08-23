#Write a python script to calculate sum of all even numbers and sum of all odd numbers of the list. List data given by user.
l=[]
n=int(input('Enter the number of element: '))
for i in range(0,n):
    m=int(input())
    l.append(m)
sum=0
sum1=0
for j in l:
    if j%2==0:
        sum=sum+j
    else:
        sum1=sum1+j
print('The sum of even: ',sum)
print('The sum of odd: ',sum1)