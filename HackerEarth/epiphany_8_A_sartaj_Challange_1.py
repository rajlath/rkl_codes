def cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

def even_cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    while i < n and j < n:
        k = 2
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 2
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

def odd_cyclic_equiv(u, v):
    n, i, j = len(u), 0, 0
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 2
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

t=int(input())
for x in range(0,t):
    f=int(0)
    n=int(input())
    l1=list(map(int,input().split(" ")))
    l2=list(map(int,input().split(" ")))
    if(set(l1)!=set(l2)):
        f=0
    else:
        if(cyclic_equiv(l1,l2)):
            f=1
            ##print("Yes")
        else:
            ##print("No")
            if(even_cyclic_equiv(l1,l2)):
                f=1
            elif(odd_cyclic_equiv(l1,l2)):
                f=1
            else:
                f=0
    if(f==1):
        print("Yes",end="\n")
    else:
        print("No",end="\n")

        