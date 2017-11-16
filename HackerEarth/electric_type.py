#copied
from sys import stdin
from collections import defaultdict
 
line_index = -1
lines = stdin.readlines()
 
 
def get_line():
  global lines, line_index
 
  line_index += 1
  return lines[line_index]
 
 
def main():
  n = int(get_line())
  A = [int(x) for x in get_line().split()]
 
  h = {}
  uniq = [0] * n
 
  for i in range(n - 2, -1, -1):
    if not h.get(A[i + 1]):
      h[A[i + 1]] = True
      uniq[i] = uniq[i + 1] + 1
    else:
      uniq[i] = uniq[i + 1]
 
  visited = {}
  ans = 0
  for i in range(n):
    if not visited.get(A[i]):
      ans += uniq[i]
      visited[A[i]] = True
 
  print(ans)
 
