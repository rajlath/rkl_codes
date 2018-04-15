'''
2
3
abc
4
abcd
'''

def encode(left, right):
    global ans
    global ins
    if left <= right:
        mid = (left + right) // 2
        ans += ins[mid]
        encode(left, mid - 1 )
        encode(mid + 1, right)

for _ in range(int(input())):
    noe = int(input())
    ins = input()
    ans = ''
    encode(0, noe-1)
    print(ans)


