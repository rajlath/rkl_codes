def foo(bbr, s):
    if s == sum(bbr):return True
    if not bbr:return False
    ans = 0
    for i in range(1, len(bbr)):
        if s == sum(bbr[:1]):
            ans += foo(bbr[i:], s)
    return ans

n = int(input())
arr = [int(x) for x in input()]
ans = 0
for i in range(1, len(arr)):
    ans += foo(arr[i:], sum(arr[:i]))
    if ans:break
print(["NO","YES"][ans])
