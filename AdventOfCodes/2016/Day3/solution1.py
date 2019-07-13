def is_valid_triangle(a, b, c):
  return  (a + b) > c and (a + c) > b and (b + c) > a

how_many = 0
ca, cb, cc = [], [],[]
for line in open("input.txt", "r"):
  a, b, c = sorted([int(x) for x in line.strip().split()])
  ca.append(a)
  cb.append(b)
  cc.append(c)
alls = ca + cb + cc
candidates = [alls[i:i + 3] for i in range(0, len(alls), 3)]
for i in range(len(alls)):
  how_many += is_v


  how_many += is_valid_triangle(a, b, c)
print(how_many)
