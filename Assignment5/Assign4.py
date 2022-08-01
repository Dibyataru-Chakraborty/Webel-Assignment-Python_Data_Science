#write a python script to print squares of numbers from a to b. values of a and b are given by user.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
for i in range(a,b+1):
    sq=i**2
    print("The square of {}: {}".format(i,sq))