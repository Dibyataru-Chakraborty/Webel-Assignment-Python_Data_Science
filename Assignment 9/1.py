def common_elements(list_1, list_2):
  a_set = set(list_1)
  b_set = set(list_2)
  if len(a_set.intersection(b_set)) > 0:
    print (list(a_set.intersection(b_set)))
  else:
    print("No common elements between the two lists")

list_one = [32, 34, 56, 65, 89, 70, 80]
list_two = [1, 2, 0, 67, 80, 89, 56]
print("Common elements between list one and list two:")
common_elements(list_one, list_two)