'''
Culprits are standing in a line.
Some of them have a claw in their hands
we know length of every claw.
At a particular time all having claw kill infrom of them with their claw.
count number of survivor


Examples
input
4
0 1 0 10
output
1
input
2
0 0
output
2
input
10
1 1 3 0 0 0 2 1 0 3
output
3
'''

nos_of_culprits = int(input())
culprits = [int(i) for i in input().split()]
survivor = 0
least = nos_of_culprits
pos = nos_of_culprits
while pos > 0:
    pos -= 1
    if pos < least:
        survivor +=1
    least = min(pos - culprits[pos], least)

print(survivor)