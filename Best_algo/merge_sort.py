def merge_sort(a)    :
    if len(a) < 2: return a
    mid = len(a) // 2
    left, right = None, None
    if a[:mid]: left = merge_sort(a[:mid])
    if a[mid:]: right=merge_sort(a[mid:])
    return merge_sort_2n(left, right)

def merge_sort_2n(left, right)    :
    if not left or not right:
        return left or right
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    return (left or right) + res[::-1]

s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
print(merge_sort(s))
