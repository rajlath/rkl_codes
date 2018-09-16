
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 10:20:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : Benjamin Baka PythonDSandAlgo Examples
# @Version : 1.0.0

def main():
    print(factorial(3))

def factorial(n):

    '''
    returns factorial of an integer n using recursion
    @param int - n
    @rets  int - factorial of n
    '''
    if n == 0:
        return 1
    fact = n * factorial(n-1)
    return fact

if __name__ == "__main__":
    main()




