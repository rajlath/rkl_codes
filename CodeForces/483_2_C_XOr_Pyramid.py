
noe = int(input())
arr = [int(x) for x in input().split()]
sum_list = [arr[0]]
for i in range(1, noe):
    sum_list.append(sum_list[i-1] + arr[i])
for _ in range(int(input())):
    l, r = [int(x)-1 for x in input().split()]
    if l == 0 and r == 1:
        print(arr[0]+arr[1])
    elif l == 0:
        print(sum_list[r] - sum_list[l+1])
    else:
        print(sum_list[r] - sum_list[l-1])


'''
from sys import stdin
# Write your code here
cases=stdin.readline()
A = [int(i) for i in stdin.readline().strip("\n").split(" ")]
sum_list=[]
sum_list.append(A[0])
for i in range(1,len(A)):
    sum_list.append(sum_list[i-1]+A[i])

n_b_queries=int(stdin.readline())
for i in range(n_b_queries):
    bounds=(int(i) for i in stdin.readline().strip("\n").split(" "))
    lowerbound=next(bounds)-1
    upperbound=next(bounds)-1
    nb_ones= sum_list[upperbound] if lowerbound==0 else sum_list[upperbound]-sum_list[lowerbound-1]
    print(nb_ones%2,upperbound-lowerbound+1-nb_ones)



arr = [1, 2, 4, 8, 16, 32]

xors = arr[1]
for i in arr[1:]:
    xors ^= i
    print(xors)
print(xors//2)

6
1 2 4 8 16 32
4
1 6
2 5
3 4
1 2
outputCopy
60
30
12
3
'''