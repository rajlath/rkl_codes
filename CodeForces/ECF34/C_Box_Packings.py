'''
Given n numbers of boxes and their length objective is reduce number
of boxes to minimum by inserting smaller boxes into larger ones.
Conditions are
Put a box i into another box j if the following conditions are met:
i-th box is not in another box already
j-th box does not have any box in it
box i is smaller than box j (ai < aj).
input
3
1 2 3
output
1
input
4
4 2 4 3
output
2
as equal size box can not be put into another box.
Startegy is to find count max size boxes.
As other smaller size boxes can be put into max size box
'''
from collections import Counter
nos_of_boxex = int(input())
boxes = [int(x) for x in input().split()]
print(max(Counter(boxes).values()))
