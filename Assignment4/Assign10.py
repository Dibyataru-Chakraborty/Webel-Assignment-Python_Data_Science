#write a python script to calculate HCF of two numbers
n1 = int(input("Entedr the 1st number: "))
n2 = int(input("Entedr the 2nd number: "))

if n1<=n2:
    min=n2

else:
    min = n1

for i in range (1,min+1):
    if n1%i == 0 and n2%i == 0:
        GCD = i

print("The HCF of two number: ",GCD)