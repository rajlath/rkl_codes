lens = int(input())
given = sorted([int(x) for x in input().split()])
needs = list(range(1, lens + 1))
moves = 0
#print(given, needs)
while given:
    moves += abs(given.pop() - needs.pop())
print(moves)
'''
n = int(input())
a = sorted(map(int, input().split()))
print(sum([abs(a[i]-i-1) for i in range(n)]))
'''
