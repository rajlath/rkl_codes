#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      rinfo
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from math import gcd

def modInverse(a, m=1000000009) :
    g = gcd(a, m)
    if (g != 1) :
        return -1
    else:
        return pow(a, m - 2, m)


n,q = map(int,input().split())
arr = {}

for _ in range(n):
  a,b = map(int, input().split())
  sol =  4*a*b+2*max(a,b)
  if sol in arr:
    arr[sol]+=1
  else:
    arr[sol] = 1

Q = list(map(int,input().split()))

for k in Q:
  sol = k*(k+1)
  if sol in arr:
    print(modInverse(arr[sol]))
  else:
    print(-1)