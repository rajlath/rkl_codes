'''
You have an array of integers
You need to perform operation on these numbers so that all becomes 1
operation: replace any two adjacent numbers with GCD of these two numbers
print number of operation needed or -1 if it can not be done
Examples
input
5
2 2 3 4 6
output
5
input
4
2 4 6 8
output
-1
input
3
2 6 9
output
4
startegy: GCD of any two numbers would be 1 if either of them is 1
or if all of them are primes
If even one 1 is avaible in array , it can be used to convert others to one
In that case nop needed is number of element -1
So first count how many 1 is available . Answer would be len array - count
In case no 1 is available startegy would be to sequentially try to convert
number with their gcd till we get 1 as gcd.
nop = nop done + length of remaining array
'''


from math import gcd
n=int(input())
a=list(map(int, input().split()))
onecnt = a.count(1)
if onecnt > 0:
    print(n - onecnt)
else:
    nop = 0
    flag=True
    while (a.count(1)==0):
        if (len(a)-nop==1 and a[0]!=1):
            flag = False
            break
        nop+=1
        for i in range(len(a)-nop):
            a[i]=gcd(a[i], a[i+1])
    print([-1,nop+n -1][flag])
