#Write a python script to print set of three words in dictionary order. Words are given by user
words = input("Enter three words: ")
word = words.split()
word.sort()
new = ""
for x in word:
    new += x + " "
print(new)