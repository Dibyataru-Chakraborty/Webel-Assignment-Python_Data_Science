# Write a python script to count vowels in the given string.

vowels = 'aeiouAEIOU'
string = "Hi, I love to eat ice cream"

string = string.casefold()
count = {}.fromkeys(vowels, 0)
for character in string:
    if character in count:
        count[character] += 1   

print(count)
