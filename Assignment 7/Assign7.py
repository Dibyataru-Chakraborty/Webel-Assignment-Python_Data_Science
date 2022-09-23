# Write a python script to check whether a given string is a palindrome or not.

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")