#copied
from sys import stdin
from collections import defaultdict
 
line_index = -1
lines = stdin.readlines()
 
def get_line():
  global lines, line_index
 
  line_index += 1
  return lines[line_index]
 
def get_mab(t1, t2, n):
  t3 = {x: 0 for x in range(1, n+1)}
 
  for i in range(1, n + 1):
    c = t2[t1[i]]
    if c != i:
      t3[c] += 1
 
  return max(t3.values())
 
def get_pairs(t1, t2, n):
  t3 = {x: 0 for x in range(1, n + 1)}
 
  ans = 0
 
  for i in range(1, n + 1):
    if t3[i] == 0:
      c = t2[t1[i]]
      d = t2[t1[c]]
      if c != i and d != c and d == i:
        ans += 1
        t3[i] = t3[c] = 1
 
  return ans
 
 
def main():
  t = int(get_line())
  for _ in range(t):
    n = int(get_line())
 
    b = {i+1: int(x) for i, x in enumerate(get_line().split())}
    g = {i+1: int(x) for i, x in enumerate(get_line().split())}
 
    x1 = get_mab(b, g, n)
    x2 = get_mab(g, b, n)
    a1 = max(x1, x2)
 
    x1 = get_pairs(b, g, n)
    x2 = get_pairs(g, b, n)
 
    print('%s %s' % (a1, x1 + x2))
 
main()
