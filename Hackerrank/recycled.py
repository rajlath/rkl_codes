s1 = "12345"
alls = [x for x in set([int(s1[n:]+s1[:n]) for n in range(len(s1))])]
print(alls)