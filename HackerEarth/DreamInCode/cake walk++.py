'''
1
5 3
1 2 3 4 5
1 3
3 4
5 1
'''

for i in range(int(input())):
    print("Case {}:".format(i+1))

    students, updates = [int(x) for x in input().split()]
    scores = [int(x) for x in input().split()]
    flag = 0
    for i in range(1, students):
        if scores[i] != scores[i-1]:flag = 1
    for _ in range(updates):
        x, y = [int(x) for x in input().split()]
        if not flag:
            print(0)
            continue
        if scores[0] == x: scores[0] = y
        sums = 0
        for i in range(1, students):
            if scores[i] == x:scores[i] = y
            sums += 2 * (abs(scores[i] - scores[i-1]))
        print(sums//2)




