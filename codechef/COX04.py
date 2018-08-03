n, m = [int(x) for x in input().split()]
t = "*"
valid=True
for i in range(n):
    curr = input().strip()
    if len(set(curr)) != 1 or curr[0] == t:
        valid = False
        break
    else:
        t = curr[0]
print("YES" if valid else "NO")