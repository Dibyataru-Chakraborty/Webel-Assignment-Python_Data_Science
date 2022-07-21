#Write a python script to calculate simple interest, data required should be taken from user
#----------------
p=int(input("Enter the principal: "))
t=int(input("Enter the time: "))
r=int(input("Enter the rate of interest: "))
i=(p*t*r)/100
print("The interest: ",i)