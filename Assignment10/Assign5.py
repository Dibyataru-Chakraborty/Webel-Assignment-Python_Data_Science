# Write a python script to take dictionary from the keyboard and print the sum of values.

n=int(input("enter number of element: "))
get = {}

for i in range(n):
    key = input("key: ")
    value = int(input("value: "))

    get[key] = value

print(sum(get.values()))
