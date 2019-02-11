nb_box, max_A, max_B = [int(x) for x in input().split()]
guddu = [int(x) for x in input().split()]
bablu = [int(x) for x in input().split()]
g_s, b_s = [], []
costs = 0
for i in range(nb_box):
    if guddu[i] >= bablu[i]:
        g_s.append(guddu[i] - bablu[i])
    else:
        b_s.append(bablu[i] - guddu[i])
    costs += max(guddu[i], bablu[i])
g_s = sorted(g_s, reverse=True)
b_s = sorted(b_s, reverse=True)
while len(g_s) > max_A:
    costs -= g_s.pop()
while len(b_s) > max_B:
    costs -= b_s.pop()
print(costs)
