lens = int(input())
weights = [int(x) for x in input().split()]
sums = sum(weights)
sum_here = 0
mins  = sums
for i in weights:
    sum_here += i
    mins = min(mins, abs(sum_here - (sums - sum_here)))
print(mins)
