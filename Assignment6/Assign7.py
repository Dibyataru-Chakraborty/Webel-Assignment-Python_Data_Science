#Write a python script to print distinct list elements along with their frequency of occurrence in the list.
li =[1,2,1,1,3,2,5,6,3,'a','a']
freq = {}
for items in li:
    freq[items] = li.count(items)
print(freq)