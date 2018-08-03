'''
3 2 3
1 3 5
2 3
1 2 3

def get_prior(arr, x):
    indx = binarySearch(arr, 0, len(arr)-1,x)
    return (indx + 1 )

def binarySearch (arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l)//2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        # Element is not present in the array
        return -1

lena, lenb, lenc = [int(x) for x in input().split()]
a = list(set([int(x) for x in input().split()]))
b = list(set([int(x) for x in input().split()]))
c = list(set([int(x) for x in input().split()]))

res = 0
for numb in b:
    res += get_prior(a, numb) * get_prior(c, numb)
print(res)
'''
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    ai = 0
    bi = 0
    ci = 0

    ans = 0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        ans += ai * ci
        bi += 1

    return ans

la, lb, lc = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
print(triplets(a, b, c))

