#print duplicate in a list
#Given a list of n numbers, print the duplicate elements in the list

#best approach : Using hashtable
from random import randint, randrange,choice, shuffle

def random_array(low, high, step, size):
    lst = []
    while len(lst)<size:
        nexts = randrange(low, high, step)
        if nexts in lst:continue
        lst.append(nexts)
    return lst

def repeating_elements(arr):
    occured_before = set()
    repeaters = []
    for i in arr:
        if i in occured_before:
            repeaters.append(i)
        else:
            occured_before.add(i)
    return repeaters

'''
arr = random_array(1, 100, 1, 40)
for i in range(4):
    arr.append(choice(arr))
print(arr)
shuffle(arr)
print(repeating_elements(arr))
'''

#Find max, appearing element in a list
#Given a list of n numbers, find the element, which appears maximum number of times.

from collections import Counter

def max_occuring_elements(arr):
    carr = Counter(arr)
    return  carr.most_common(1)[0]


'''
arr = random_array(1, 100, 1, 40)
src = randint(1, 40)
for i in range(5):
    arr.append(src)
shuffle(arr)
max_occured, times_occured = max_occuring_elements(arr)
print("{} has occured {} times".format(max_occured, times_occured))
'''

# Majority element in a list
# Given a list of n elements. Find the majority element, which appears more than n/2 times. Return
# 0 in case there is no majority element.



def getMajority(arr):
    size = len(arr)
    majIndex = size // 2
    i = 0
    arr.sort()
    candidate = arr[majIndex]
    count = arr.count(candidate)
    if count <= size // 2:
        return -1
    else:
        return candidate # can also raised exception.

#print(getMajority([2, 12, 2, 2, 11,2]))

# Find the missing number in a list
# Given a list of n-1 elements, which are in the range of 1 to n. There are no duplicates in the list.
# One of the integer is missing. Find the missing element.

#given a sequence of consecutive numbers find which number is missing

def find_missing(arr):
    size = len(arr)
    maxv = max(arr)

    xor_sum = 0
    for i in range(1, maxv+1):
        xor_sum ^= i
    for i in range(size):
        xor_sum ^= arr[i]
    return xor_sum
arr = list(range(25))
arr.remove(12)
#print(find_missing(arr))

#Find Pair in a list
#given a list of n numbers, find two elements such that their sum is equal to “value”

def find_pair(arr, val):
    prospectives = set()
    for i in arr:
        if (val - i) in prospectives:
            return i, val - i
        else:
            prospectives.add(i)
    return -1,-1
'''
arr = random_array(1, 100, 1, 40)
val1 = choice(arr)
val2 = choice(arr)
val = val1 + val2
print(arr, val1, val2)
print(find_pair(arr, val))
'''

#Find the Pair in two Lists
#Given two list X and Y. Find a pair of elements (xi, yi) such
#that xi∈X and yi∈Y where xi+yi=value.

from collections import defaultdict
from random import randint, randrange,choice, shuffle

def random_array(low, high, step, size):
    lst = []
    while len(lst)<size:
        nexts = randrange(low, high, step)
        if nexts in lst:continue
        lst.append(nexts)
    return lst
def find_pair_from_two_list(a, b, val):
    b_dict = defaultdict(int)
    for i,v in enumerate(b): b_dict[v] = i
    for v in a:
        if (val - v) in b_dict:
            return v, val-v
    return -1, -1
'''
arr1 = random_array(1, 100, 1, 99)
arr2 = random_array(1, 100, 1, 99)
val1 = choice(arr1)
val2 = choice(arr2)
val = val1 + val2
print(arr1,arr2,  val1, val2)
print(find_pair_from_two_list(arr1,arr2, val))
'''
#Two elements whose sum is closest to zero
#Given an List of integer s, both +ve and -ve. You need to find the two elements such that their
#sum is closest to zero.



























