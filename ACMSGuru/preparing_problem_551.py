#TLE
n, t1, t2 = [int(x) for x in input().split()]
a = 0
t = 0
f1 = True
f2 = True
while (f1 | f2):
    t += 1
    if f1 and (t%t1==0):a+=1
    if f2 and (t%t2==0):a+=1
    if f1 and (t%t1==0) and a >= n: f1 = False
    if f2 and (t%t2==0) and a >= n: f2 = False
print(a, t)



