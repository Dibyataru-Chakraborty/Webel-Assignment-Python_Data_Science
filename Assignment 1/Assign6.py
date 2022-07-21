#Write a python script to calculate area of triangle, length of the sides is given by user
#----------
import math
l1=int(input("Enter the 1st length: "))
l2=int(input("Enter the 2nd length: "))
l3=int(input("Enter the 3rd length: "))
s=(l1+l2+l3)/2
a=math.sqrt(s*(s-l1)*(s-l2)*(s-l3))
print("The area of triangle: ",a)