from collections import Counter
for _ in range(int(input())):
    nob = int(input())
    ans = Counter([int(x) for x in input().split()]).most_common()
    print(len(ans), ans[0][1])