from collections import Counter
for _ in range(int(input())):
    cnts = int(input())
    pile = Counter([int(x) for x in input().split()])
    largest = pile.most_common()[0][1]
    print(cnts - largest)
