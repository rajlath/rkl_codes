'''
8
11010111
'''
ln = int(input())
s = [int(x) for x in input()]
cnt = 0
for i in range(ln):
    for j in range(i+1, ln):
        curr = s[i:j]
        lns = len(curr)
        ones = curr.count(1)
        if ones*2 == lns:
            cnt = max(cnt, lns)
print(cnt)            
            
