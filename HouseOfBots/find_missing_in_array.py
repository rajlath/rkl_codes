def find_missing_in_array(arr):
    '''
    given an array of continious whole numbers with one
    element missing, find the missing element.
    type  : array of integers, sorted and continious
    rtype : integer
    '''
    nb_elements  = max(arr)
    sum_of_array = sum(arr)
    should_be_sum= (nb_elements * (nb_elements + 1)) // 2
    return should_be_sum - sum_of_array


arr = list(range(1, 123456))
del arr[9856]
print(find_missing_in_array(arr))

#PS C:\Users\rinfo> python -u "e:\rkl_codes\HouseOfBots\find_missing_in_array.py"
#9857



