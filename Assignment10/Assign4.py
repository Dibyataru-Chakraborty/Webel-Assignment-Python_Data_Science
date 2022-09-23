# Write a python script to sort a dict according to VALUE.

a={ 2:'apple', 4:'grapes', 1:'mango',3:'orange', 11: 'Dibyataru', 31:'Bhaskar', 5:'Sagnik', 8:'Raja'}

c=sorted(a.items(), key=lambda x:x[1])

for i,j in c:
    print(i,':', j)
