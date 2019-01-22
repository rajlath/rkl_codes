i = input()
t=int(input())
maybe = []
s=[input() for _ in range(t)]
for x in s:
    for y in s:
        curr = (x + y)
        maybe.append(curr[1:3])
print(maybe)