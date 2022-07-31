#write a python script to check whether two given numbers are co-prime or not
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
if n1<=n2:
        min=n2
else:
    min = n1
for i in range (1,min+1):
    if n1%i == 0 and n2%i == 0:
        GCD = i
if GCD==1:
    print("The numbers are co-prime")
else:
    print("The numbers are not co-prime")
