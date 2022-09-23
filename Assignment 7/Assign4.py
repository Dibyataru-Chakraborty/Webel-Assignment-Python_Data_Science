# Write a python script to count occurrence of a given character in the given string

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
    
print("The total Number of ", char, " = " , count)