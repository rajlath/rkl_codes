sl= int(input())
s = input()

cnt =0
a = [0]*33
for i in range(sl-2): 
    for j in range(i+2,sl):
        if s[i] == s[j]:
            for k in range(i+1, j):
                cnt += a[ord(s[k]) - ord('a')]
    a[ord(s[i]) - ord('a')]+= 1
print(cnt) 
'''
34
hylobclddzflmzitrxwwsqhozvgexhxjmm  

36 
'''
    
