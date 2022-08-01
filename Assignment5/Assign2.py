#write a python script to print a table of user's choice.
n=int(input("Enter the number to to print table: "))
for i in range(1,11):
    mul=n*i
    print("{} x {}=".format(n,i),end=" ")
    print(mul)