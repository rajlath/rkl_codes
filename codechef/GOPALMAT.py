nb_bldg, nb_query = [int(x) for x in input().split()]
buildings = [int(x) for x in input().split()]
stack = [0]
visible = [0] * (nb_bldg + 1)
for i, v  in enumerate(buildings):
    if v > stack[-1]:
        visible[i] = visible[i-1] + 1
        stack.append(v)
    else:
        visible[i] = visible[i-1]
for _ in range(nb_query):
    l, r = [int(x) for x in input().split()]
    print(visible[r] - visible[l-1])
