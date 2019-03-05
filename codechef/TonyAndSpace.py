'''
def canPartition3subsets(arr, k= 3):
    target, rem = divmod(sum(arr), 3)
    if rem: return False
    def search(groups):
        if not arr: return True
        v = arr.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if search(groups):return True
                groups[i] -= v
            if not group:break
        arr.append(v)
        return False
    arr.sort()
    if arr[-1] > target: return False
    while arr and arr[-1] == target:
        arr.pop()
        k -= 1
    return search([0] * 3)

lens = int(input())
arrs=[int(x) for x in input().split()]
print(canPartition3subsets(arrs))
'''

nb_element = int(input())
elements   = sorted([int(x) for x in input().split()], reverse=True)
elem_sum   = sum(elements)
need_sum   = elem_sum // 3
result     = elem_sum % 3 == 0
if result:
    members = [0] * 3
    for elem in elements:
        for i in range(3):
            if members[i] + elem <= need_sum:
                members[i] += elem
                break
    result = set(members) == {need_sum}
if result:
    print("Yes")
    print(need_sum)
else:
    print("No")


