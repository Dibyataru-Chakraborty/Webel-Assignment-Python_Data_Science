list = ["a", "ab", "a", "abc", "ab", "ab"]

def countOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

print(countOccurrence(list))