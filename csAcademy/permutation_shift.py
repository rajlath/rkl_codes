'''
6
2 3 4 6 1 5
3
'''
element_count = int(input())
elements      = [int(x)-1 for x in input().split()]
best = 0
for i in range(element_count):
    match_count = 0
    for j in range(element_count):
        match_count +=  elements[(j + i) % element_count] == j
    best = max(best, match_count)
print(best)