import random
def create_random_int_arr(element_count, range_start, range_end, distinct= True):
    '''
    create an array of integers haveing number of element=element_count
    having values between range_start and range_end - inclusive

    :type element_count int
    :type range_start   int
    :type range_end     int
    :rtype [] of int
    '''
    if distinct:
        return random.sample(range(range_start, range_end+1), element_count)
    else:
        return [random.randint(range_start, range_end+1) for _ in range(element_count)]


