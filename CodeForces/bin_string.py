a, b, x = [int(x) for x in input().split()]
s = '0'
a -= 1
while x > 0:
    nexts = ["0", "1"][s[-1] == "0"]
    if nexts == "0" and a > 0 :
        s += "0"
        a -= 1
        x -= 1
    if nexts == "1" and  b > 0:
        s += "1"
        b -= 1
        x -= 1
#print(s)
if a > 0:
    for i,v in enumerate(s):
        if v == "0":
            s = s[:i] + "0" * a + s[i:]
            break
if b > 0:
    for i, v in enumerate(s):
        if v == "1":
            s = s[:i] + "1" * b + s[i:]
            break
print(s)









