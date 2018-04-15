'''
Input:
2
abcd
rahul

Output:
)!@#
&)&)!
'''
symbols = ")!@#$%^&*("
for _ in range(int(input())):
    s = input().strip()
    a = ''
    for sc in s:
        a += symbols[(ord(sc) - ord('a'))%10]
    print(a)
