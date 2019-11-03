a,m,n,d = [int(x) for x in input().split()]
fare = 0
if d > a:
    fare += m
    d -= a
    fare += n * d
else:
    fare = d * m
print(fare)