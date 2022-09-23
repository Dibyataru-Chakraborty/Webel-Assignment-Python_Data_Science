# Write a python script to reverse a string.

str=input("Enter a String: ")

n=""

for i in str:
	n = i + n

print(n)