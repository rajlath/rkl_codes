'''
Input
2 47

Output
NO
Input
4 4738

Output
NO
Input
4 4774

Output
YES
'''

ans   = "YES"
noe, nums = [x for x in input().split()]
for x in nums:
    if x not in ["4", "7"]:
        ans = "NO"
        break
if ans == "YES":
    if (sum([int(x) for x in nums[:int(noe)//2]]) != sum([int(x) for x in nums[int(noe)//2:]])):
        ans = "NO"
print(ans)
