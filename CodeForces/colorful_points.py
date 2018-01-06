'''
You are given a set of points on a straight line. Each point has a color assigned to it.
For point a, its neighbors are the points which don't have any other points between them and a.
Each point has at most two neighbors - one from the left and one from the right.
You perform a sequence of operations on this set of points. In one operation, you delete all points which have a
neighbor point of a different color than the point itself. Points are deleted simultaneously,
i.e. first you decide which points have to be deleted and then delete them. After that you can perform the next operation etc. If an operation would not delete any points, you can't perform it.

How many operations will you need to perform until the next operation does not have any points to delete?

Input
Input contains a single string of lowercase English letters 'a'-'z'.
The letters give the points' colors in the order in which they are arranged on the line:
the first letter gives the color of the leftmost point, the second gives the color of the second point from the left etc.

The number of the points is between 1 and 106.

Output
Output one line containing an integer - the number of operations which can be performed on the given set of points until there are no more points to delete.

Examples
input
aabb
output
2
input
aabcaa
output
1
Note
In the first test case, the first operation will delete two middle points and leave points "ab", which will be deleted with the second operation. There will be no points left to apply the third operation to.

In the second test case, the first operation will delete the four points in the middle, leaving points "aa". None of them have neighbors of other colors, so the second operation can't be applied.
'''



s = input()
n = 1

for i in range(1, len(s)):
  if s[i] != s[i-1]:
    n += 1

mas = [0] * n
col = [0] * n

count = 1
idx = 0
c = s[0]
for i in range(1, len(s)):
  if s[i] == s[i-1]:
    count += 1
  else:
    mas[idx] = count
    col[idx] = c
    idx += 1
    count = 1
    c = s[i]

mas[idx] = count
col[idx] = c

res = 0

while n > 1:
  newlen = n
  idx = -1

  for i in range(0, n):
    if (i == 0) or (i == n - 1):
      mas[i] -= 1
    elif mas[i] >= 2:
      mas[i] -= 2
    else:
      mas[i] = 0

    if mas[i] == 0:
      newlen -= 1
    else:
      if idx >= 0 and col[idx] == col[i]:
        mas[idx] += mas[i]
        newlen -= 1
      else:
        idx += 1
        mas[idx] = mas[i]
        col[idx] = col[i]
        type = i % 2

  n = newlen
  res += 1

print(res)