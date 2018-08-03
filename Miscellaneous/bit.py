'''
implementation of BIT in python
1. create BIT
2. helpers Update : Update function to create/ update BIT
3. helpers Sums   : Get Sum of elements from 0 to index
'''
arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

def update_bit(BITree, n, i,  v):
    '''
    update BIT with a value v at index n
    update means adding value v to the elements at index i
    type BITree : BIT to be updated due to update of array element
    type n : int - length of the arr to be updated
    type i : int - index of the arr which is to be updated
    type v : int - value with which arr[i] is to be updated
    '''
    i += 1
    while i < n:
        BITree[i] += v
        i += i & (-i)

def construct_bit(arr, n):
    '''
    construct BIT for array arr having length n
    type arr : array of integers
    type n   : int : length of arr
    rtype    : BIT
    '''
    BTree = [0] * (n + 1)
    for i in range(n):
        update_bit(BTree, n, i, arr[i])
    return BTree

def get_sum(BTree, i):
    '''
    get sums of elements in the range 0 .. i
    type BTree: Binary Tree for the array
    type i : int  sum of the array elements till index i
    rtyep  : int sum
    '''
    sums = 0
    i += 1
    while i > 0:
        sums += BTree[i]
        i -= i & (-i)
    return sums

def get_range_sum(BTree, l, r):
    '''
    get sums of the elements in the range l, r
    type BTree : binary tree of the array
    type l     : int start index
    type r     : int end   index
    rtyep  s   : int sums for the range
    '''
    return get_sum(BTree, r) - get_sum(BTree, l - 1)
print(arr)
BTree = construct_bit(arr, len(arr))
print(BTree)
print(get_sum(BTree, 5))
update_bit(BTree, len(arr), 3, 6)
print(get_sum(BTree, 5))




