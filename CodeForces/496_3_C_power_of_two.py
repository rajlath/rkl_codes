s = input()
p = 0
n = 0
for i in s:
    n += int(i)
    if not n%3 or not int(i)%3 or not (n%100)%3:
        p, n = p+1, 0
    else:
        n*= 10
print(p)