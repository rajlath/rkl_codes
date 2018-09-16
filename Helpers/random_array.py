import random
from string import ascii_uppercase as uc, ascii_lowercase as lc, ascii_letters as ll, digits as ds, punctuation as pu
def create_random_int_arr(element_count, range_start, range_end, distinct= True):
    '''
    create an array of integers haveing number of element=element_count
    having values between range_start and range_end - inclusive
    To have all distinct elements - default behaviour.
    To have repeating elements  distinct is set to false.

    :type element_count int
    :type range_start   int
    :type range_end     int
    :type distinct      boolean
    :rtype [] of int
    '''
    if distinct:
        return random.sample(range(range_start, range_end+1), element_count)
    else:
        return [random.randint(range_start, range_end+1) for _ in range(element_count)]

def create_random_chr_array(arr_length,ch_case='',has_digits=False, has_punctuation=False):
    elems = ''
    if   ch_case == "l": elems += lc
    elif ch_case == "u": elems += uc
    else: elems += ll
    if has_digits : elems += ds
    if has_punctuation : elems += pu
    #return "".join(random.choice(elems) for _ in range(arr_length))
    return [''.join(random.sample(elems, 1)) for _ in range(arr_length)]



def create_random_str_array(arr_length,ch_case='',has_digits=False, has_punctuation=False,ers=1,ere=10):
    '''
    create an array of string

    :type arr_length       int      :length of array
    :type ch_case          ch       :'l' : only lower case, 'u' : only upper case default :blank both case
    :type has_digits       boolean  :to include digits set to True - default false
    :type has_punctuation  boolean  :to include punctuation set to True - default False
    :type ers:element      int      :length range start
    :type ere:element      int      :length range end

    :rtype array of string
    '''

    elems = ''
    if   ch_case == "l": elems += lc
    elif ch_case == "u": elems += uc
    else: elems += ll
    if has_digits : elems += ds
    if has_punctuation : elems += pu
    #return "".join(random.choice(elems) for _ in range(arr_length))
    return [''.join(random.sample(elems, random.randint(ers, ere) )) for _ in range(arr_length)]







