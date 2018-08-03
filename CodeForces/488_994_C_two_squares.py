'''
Examples
inputCopy
0 0 6 0 6 6 0 6
1 3 3 5 5 3 3 1
outputCopy
YES
inputCopy
0 0 6 0 6 6 0 6
7 3 9 5 11 3 9 1
outputCopy
NO
inputCopy
6 0 6 6 0 6 0 0
7 4 4 7 7 10 10 7
outputCopy
YES
'''
class A(object):
    def __init__(self, arr):
        self.X = max(arr[::2])
        self.x = min(arr[::2])
        self.Y = max(arr[1::2])
        self.y = min(arr[1::2])
    def has(self, a, b):
        return self.x <= a and a <= self.X and self.y <= b and b <= self.Y
        #return self.x <= a <= self.X and  self.y <= b <= self.Y
class B(object)        :
    def __init__(self, arr):
        self.x    = sum(arr[::2]) // 4
        self.y    = sum(arr[1::2]) // 4
        print(self.x, self.y)
        self.first = arr[0]
        self.nexts = arr[1]

    def distance(self, a, b)    :
        return abs(a - self.x) + abs(b - self.y)

    def has(self, a, b):
        self.distance(a, b) <= self.distance(self.first, self.nexts)


a = A([int(x) for x in input().split()])
b = B([int(x) for x in input().split()])
print(a, b)
ans = "NO"
for i in range(-100, 101):
    for j in range(-100, 101):
        if a.has(i, j) and b.has(i, j):
            print("here")
            ans = "YES"
            break
print(ans)

