'''
Build the Fence
Time limit: 1000 ms
Memory limit: 256 MB

You have NN wooden boards, having the same width, but different heights. You can take any wooden board and cut in two, as long as the resulting two wooden boards have integer heights. The cut can only be performed horizontally, so the two resulting boards will have the same width as the initial one.

Your goal is to build a fence consisting of KK boards, all having the same height. What's the maximum height of the boards in the fence?

Standard input
The first line contains two integers NN and KK.

The second line contains NN integers representing the initial heights of the NN wooden boards.

Standard output
If there is no solution, output 00.

Otherwise, print the answer on the first line.

Constraints and notes
1 \leq N \leq 10^51≤N≤10
​5
​​
1 \leq K \leq 10^{14}1≤K≤10
​14
​​
The heights are integers between 11 and 10^910
​9
​​
Input	Output	Explanation
3 4
15 10 8
7
Cut the boards the following way:

15->7, 7, 115−>7,7,1

10->7, 310−>7,3

8->7, 18−>7,1

This way, there are 44 boards of height 77 which can be used to build a fence of maximum height.

3 5
1 1 1
0
Note that there's no solution, so the answer is 00.

3 1
10 10 10
10
Any board can be used to build a fence.

3 4
100 5 10
25
Cut the board of height 100100 into 44 boards of height 2525.
'''
n, k = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]

left = 0
rite = int(10e14)

while left != rite:
    mid = (rite + left +1) // 2
    cnt = 0
    for i in arr:
        cnt += i//mid
    if cnt >= k: left = mid
    else: rite = mid - 1
print(left)

