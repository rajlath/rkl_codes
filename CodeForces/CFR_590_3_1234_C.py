'''
Sample Input
20
30 8
50 10

Sample Output

80
'''
max_wt = int(input())
it1_val, it1_wt = [int(x) for x in input().split()]
it2_val, it2_wt = [int(x) for x in input().split()]
ans = 0
if it1_wt < max_wt:
    if it2_wt < max_wt:
        if it1_wt + it2_wt <= max_wt:
            ans = it1_val + it2_val
        else:
            ans = max(it1_val, it2_val)
    else:
        ans = it1_val
else:
    if it2_wt < max_wt:
        ans = it2_val
print(ans)


