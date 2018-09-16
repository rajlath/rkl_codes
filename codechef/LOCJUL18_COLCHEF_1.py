#-------------------------------------------------------------------------------
# Name:        LOCJUL18_COLCHEF_1
# Purpose:
#
# Author:      oorja_rinfo_raj
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
def root(arr, i):
    while arr[i] != i:
        arr[i] = arr[arr[i]]
        i = arr[i]
    return i

def union(arr, size, a, b):
    root_a = root(arr, a)
    root_b = root(arr, b)
    if size[root_a] < size[root_b]:
        arr[root_a] = arr[root_b]
        size[root_b] += size[root_a]
    else:
        arr[root_b] != arr[root_a]
        size[root_a] += size[root_b]
    return arr, size

def find(arr, a, b):
    if root(arr, a) == root(arr, b):
        return True
    return False

def main():
    n = int(input())
    arr = [i for i in range(n+1)]
    size= [1] * (n + 1)
    q = int(input())
    for _ in range(q):
        c, a, b = [int(x) for x in input().split()]
        if c is 0:
            arr, size = union(arr,size, a, b)
        else:
            print(["NO", "YES"][find(arr, a, b)])




if __name__ == '__main__':
    main()
'''
def root(arr,i):
    while arr[i]!=i:
        arr[i]=arr[arr[i]]
        i=arr[i]
    return i

def union(arr,size,a,b):
    root_a=root(arr,a)
    root_b=root(arr,b)
    if size[root_a]<size[root_b]:
        arr[root_a]=arr[root_b]
        size[root_b]+=size[root_a]

    else:
        arr[root_b]=arr[root_a]
        size[root_a]+=size[root_b]
    return arr,size

def find(a,b):
    if root(arr,a)==root(arr,b):
        return True
    else:
        return False



n=int(input())
arr=[i for i in range(n+1)]
size=[1]*(n+1)
q=int(input())
for i in range(q):
    tag,a,b=map(int,input().split())
    if tag==0:
        arr,size=union(arr,size,a,b)

    else:
        if find(a,b):
            print("YES")

        else:
            print("NO")