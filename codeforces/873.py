n,k,x = [int(x) for x in input().split()]
chores= [int(x) for x in input().split()]
times = sum(chores[:n-k]) + (k * x)
print(times)
