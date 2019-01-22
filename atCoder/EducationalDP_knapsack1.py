nb_items, max_weight = [int(x) for x in input().split()]
weights  =  []
values   =  []
for _ in range(nb_items):
    w, v = [int(x) for x in input().split()]
    weights.append(w)
    values.append(v)
dp = [0 for x in range(max_weight + 1)]
for i in range(nb_items):
    for j in range(max_weight, weights[i], -1):
        dp[j] = max(dp[j], values[i] + dp[j - weights[i]])
print(dp)