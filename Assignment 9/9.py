def cartesianProduct(set_a, set_b):
    result =[]
    for i in range(0, len(set_a)):
        for j in range(0, len(set_b)):
            if type(set_a[i]) != list:        
                set_a[i] = [set_a[i]]
            temp = [num for num in set_a[i]]   
            temp.append(set_b[j])            
            result.append(temp) 
             
    return result
def Cartesian(list_a, n):
    temp = list_a[0]
    for i in range(1, n):
        temp = cartesianProduct(temp, list_a[i])
         
    print(temp)
list_a = [[1, 2],          
          ['A'],          
          ['x', 'y', 'z']]   
n = len(list_a)
Cartesian(list_a, n)