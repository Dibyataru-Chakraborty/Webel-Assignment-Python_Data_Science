#Write a python script to check nature of roots of a given quadratic equation
import cmath
a=int(input("Enter the number of a: "))
b=int(input("Enter the number of b: "))
c=int(input("Enter the number of c: "))
if a==0:
    print("a cannot be 0")
else:
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))