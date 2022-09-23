# Write a python script to remove duplicate characters from a given string.

string=input("Enter a String: ")
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)
