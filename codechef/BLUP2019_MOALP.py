counts = [0]
count  = 0
for i in range(1, 2000001):
    curr = i
    while curr > 0:
        mod = curr % 16
        if mod > 9 and mod < 16: count += 1
        curr//=16
    counts.append(count)

nb_test = int(input())
for  _ in range(nb_test):
    l, r = [int(x) for x in input().split()]
    print(counts[r] - counts[l-1])













