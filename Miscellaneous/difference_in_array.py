# Given two non-zero elements array, output an array consist of
# of all elements thats in one array but not in another.
def difference_in_array_1(a, b):
    '''
    solution 1 will use set operation difference
    param a : array of int
    param b : array of int
    return array of int
    '''
    return list(set(a).difference(set(b)))+list((set(b).difference(set(a))))

def difference_in_array_2(a, b):
    '''
    solution 2 concate both the list
    iterate this list and add to result if item in this list
    is not in either a or not in b
    '''
    return [x for x in a+b if x not in a and x in b or x in a and x not in b]

def difference_in_array_3(a, b):
    '''
    iterate both the list
    add elements to result if its not in other list
    '''
    res = []
    for i in a:
        if i not in b:res.append(i)
    for i in b:
        if i not in a:res.append(i)
    return res





a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
print(difference_in_array_1(a, b))
print(difference_in_array_2(a, b))
print(difference_in_array_3(a, b))