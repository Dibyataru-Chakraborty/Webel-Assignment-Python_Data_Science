#Write a python script to take month value in numeric format and display number of days in it
month = int(input())
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	print("Number of days is 31")
	print("Number of days is 29")
elif(month == 2):
	print("Number of days is 28 or 29")
else:
	print("Number of days is 30")
