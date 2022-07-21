#Write a python script to check if a year is leap year or not
n=int(input("Enter the year: "))
if n%400==0 or n%4==0 and n%100!=0:
    print ("The year is leap year")
else:
    print ("The year is not leap year")