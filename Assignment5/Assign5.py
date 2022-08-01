#write a python script to print a sequence of number with given step size boundary values. 
#For example boundary values are 10 and 30, step is 2 then your output should be 10,12,14,16,18,20,22,24,26,28,30
a=int(input("Enter start number: "))
b=int(input("Enter end number: "))
c=int(input("Enter step number: "))
for i in range(a,b+1,c):
    print(i,end=" ")