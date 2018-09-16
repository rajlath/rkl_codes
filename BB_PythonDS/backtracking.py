
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 10:20:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : Benjamin Baka PythonDSandAlgo Examples
# @Version : 1.0.0

def main():
    print(bit_str("abc", 3))

def bit_str(s, l):

    '''
    returns a set of permutation ( of a length ) of a string
    @param str - s
    @param int - l : length of each element
    @rets  set
    '''
    if l == 1: return s
    return [ digit + bits for digit in bit_str(s, 1)for bits in bit_str(s, l - 1)]

if __name__ == "__main__":
    main()




