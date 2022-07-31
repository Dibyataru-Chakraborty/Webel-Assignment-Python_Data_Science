#write a python script to print first N even natural numbers in reverse order using range function in for loop.
n = int(input("Enter the number: "))
print("The first N even natural numbers: ")
for i in range(n,1,-1):
    if i%2==0:
        print(i,end=" ")