'''
you have a number of leftover cola cans.
you know capacity of these cans.
can you fill ALL cola remaining in cans in at most two cans.

Examples
input
2
3 5
3 6
output
YES
input
3
6 8 9
6 10 12
output
NO
input
5
0 0 5 0 0
1 1 8 10 5
output
YES
input
4
4 1 0 3
5 2 2 3
output
YES
'''
nos_of_cans = int(input())
left_overs =  [int(x) for x in input().split()]
capacities =  [int(x) for x in input().split()]
sum_left_overs = sum(left_overs)
sorted_capacities = sorted(capacities)
if sum(sorted_capacities[-2:]) >= sum_left_overs:
    print("Yes")
else:
    print("No")

