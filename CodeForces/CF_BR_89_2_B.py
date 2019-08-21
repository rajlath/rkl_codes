n = int(input())
s = "0123456789"
current = s[:n] + s[n::-1]
for i in current:
    curr = int(i)
    currs = " ".join(" " * (n - curr) + s[:curr] + s[curr::-1])
    print(currs)
