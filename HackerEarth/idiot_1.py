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
  arr = [i for i in range(256)]
  table = {chr(k): k for k in range(256)}
 
  for _ in range(n):
    x, y = get_line().strip().split()
 
    a, b = table[x], table[y]
    arr[a], arr[b] = arr[b], arr[a]
    table[x], table[y] = b, a
 
  map = {}
  for idx, v in enumerate(arr):
    map[chr(idx)] = chr(v)
  print(arr, table)   
 
  s = get_line().strip()
  ans = []
 
  for c in s:
    if c.islower():
      ans.append(map[c.upper()].lower())
    else:
      ans.append(map[c])
 
  print(''.join(ans))
 
main()
