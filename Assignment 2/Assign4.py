#Write a python script to find greatest among three numbers
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))
n3=int(input("Enter the 3rd number: "))
if n1>n2 and n1>n3:
    print("The {0} number is greatest".format(n1))
elif n2>n1 and n2>n3:
    print("The {0} number is greatest".format(n2))
else:
    print("The {0} number is greatest".format(n3))