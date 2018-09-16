'''
Example
Input:


3

5

2

4


Output:


3 5

1 2

1 3

'''

from math import log
for _ in range(int(input()))    :
    n = int(input())
    ind = log(n) // log(2)
    num = int(pow(2, ind))
    find= n - num
    find = 2 * find + 1
    if find > num:
        print(find, find - num)
    else:
        print(find, find + num//2)

