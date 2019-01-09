# Parameter n is an integer
# The function should return a string
from functools import reduce
from operator import mul

def product_of_five(array):
    array = sorted(array)
    candidate_1 = reduce(mul, array[-5:])
    print()
    arr = array[0:2] + array[-3:]
    
    candidate_2 = reduce(mul, arr)
    arr =  array[:4] + [array[-1]]
    candidate_3 = reduce(mul, arr)
    return max(candidate_1, candidate_2, candidate_3)
    
n = int(input())
array = list(map(int, input().split(' ')))
answer = product_of_five(array)
print(answer)



    
  
    
    
    
