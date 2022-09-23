def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]

def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)==n]
 
if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    n = 3
    print(subsets_of_given_size(numbers, n))