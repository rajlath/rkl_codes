'''
Examples
inputCopy
512 4
outputCopy
50
inputCopy
1000000000 9
outputCopy
1
'''
num, k = [int(x) for x in input().split()]
while k > 0:
    if num%10>0:num-=1
    else:num//=10
    k-= 1
    #print(num, k)
print(num)