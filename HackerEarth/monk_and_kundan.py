'''
SAMPLE INPUT 
3
aA1 b
a b c d
aa BB cc DD
SAMPLE OUTPUT 
132
24
640
'''


intial = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    arr = [x for x in input().split()]
    sums = 0
    for i in arr:
        curr = i
        sum1 = 0
        for k, v in enumerate(curr):
            sum1 += (k + intial.index(v))
        sums += sum1
    sums *= len(arr) 
    print(sums)               
    
