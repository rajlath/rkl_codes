'''
lines, width = [int(x) for x in input().split()]
for i in range(lines):
    res = i % 4

    if res in [0, 2]:
        print("#"*width)
    if res == 1:
        print("."*(width - 1)+"#")
    if res == 3:
        print("#"+"."*(width - 1))

#print(4 - len(set([int(x) for x in input().split()])))


if sorted(input() + input()) == sorted(input()):
    print("Yes")
else:
    print("No")

nos = int(input())
res = input()
a = res.count("A")
b = res.count("D")
ans = "Friendship"
if a > b:ans = "Anton"
if b > a:ans = "Danik"
print(ans)

input
4 3
3 2 3
output
6

houses, tasks = [int(x) for x in input().split()]
all_tasks = [int(x) for x in input().split()]
times = 0
start = 1
for i in range(len(all_tasks)):
    times += (all_tasks[i] - start + houses)%houses
    start = all_tasks[i]
print(times)

3 7
4 5 14

nof, maxh = [int(x) for x in input().split()]
friends   = [int(x) for x in input().split()]
width = 0
for i in friends:
    width += [2, 1][i <= maxh]
print(width)

input
2 2
1 99
100 0
output
YES

strength, demons = [int(x) for x in input().split()]
ans = "YES"
for _ in range(demons):
    x, y = [int(x) for x in input().split()]
    if x < strength:
        strength+= y
    else:
        ans = "NO"
        break
print(ans)

s,'''
n=map(int,input().split())
x,y=zip(*sorted(tuple(map(int,input().split())) for i in range(n)))
print(['NO','YES'][all(s+sum(y[:i])>x[i] for i in range(n))])