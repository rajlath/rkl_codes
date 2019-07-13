'''
def is_valid_triangle(a, b, c):
  return  (a + b) > c and (a + c) > b and (b + c) > a

how_many = 0
ca, cb, cc = [], [],[]
for line in open("input.txt", "r"):
  a, b, c = [int(x) for x in line.strip().split()]
  ca.append(a)
  cb.append(b)
  cc.append(c)
alls = ca + cb + cc
candidates = [alls[i:i + 3] for i in range(0, len(alls), 3)]
print(candidates)
for i in candidates:
  how_many += is_valid_triangle(i[0], i[1], i[2])
print(how_many)
'''
data = [[float(y) for y in x.strip().split()] for x in open('input.txt').readlines()]

def solve1():
    count = 0
    for line in data:
        line = sorted(line)
        if line[0] + line[1] > line[2]:
            count += 1
    return count

def solve2():
    my_triangles = []
    for i in range(0, len(data), 3):
        block = data[i:i+3]
        for j in range(0, 3):
            t1 = []
            for k in range(0, 3):
                t1.append(block[k][j])
            my_triangles.append(t1)

    count = 0
    for line in my_triangles:
        line = sorted(line)
        if line[0] + line[1] > line[2]:
            count += 1
    return count




if __name__ == "__main__":
    #print(solve1())
    print(solve2())


