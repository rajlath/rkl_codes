'''
Input
2
3
15 20 60 75 80 100
4
9 9 12 12 12 15 16 20

Output
Case #1: 15 60 75
Case #2: 9 9 12 15
'''

in_file = open("A-small-practice.in", "r")
ou_file = open("A-small-practice.ou", "w")
case_cnt = int(in_file.read().strip())
for case in range(case_cnt):
    sale_cnt = int(input())
    items    = sale_cnt * 2
    prices   = [int(x) for x in input().split()]
    could_be = []
    for i in range(len(prices)):
        curr = prices[i]
        if not curr % 3 and curr != -1:
            for j in range(i+1, len(prices)):
                if 


case_cnt = int(input())
for case in range(case_cnt):
    sale_cnt = int(input())
    items    = sale_cnt * 2
    prices   = [int(x) for x in input().split()]
    could_be = []
    for i in range(items):
        curr = prices[i]
        if curr % 3 == 0 and curr != -1:
            for j in range(i+1,items):
                if prices[j] == (curr // 3) * 4:
                    could_be.append(curr)
                    prices[i] = -1
                    prices[j] = -1
                    break
        else:
            if curr % 4 == 0 and curr != -1:
                for j in range(i+1, items):
                    if prices[j] == (curr // 4) * 3:
                        could_be.append(prices[j])
                        prices[i] = -1
                        prices[j] = -1
                        break
    print(could_be)


