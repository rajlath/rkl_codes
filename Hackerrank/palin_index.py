'''
Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
'''

for _ in range(int(input())):
    s = input()
    res = -1
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i - 1]:            
            a = s[:i]+s[i+1:]
            if a == a[::-1]:
                res = i
                break            
            b = s[:len(s)-i-1] + s[len(s)-i:]
            if b == b[::-1]:
                res = len(s) -i -1
                break
    print(res)                 
