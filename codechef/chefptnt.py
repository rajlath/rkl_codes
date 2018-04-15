'''
2
4 4 2 4
EEOO
4 3 1 4
EEOO
'''

for _ in range(int(input())):
    n, m, x, k = [int(x) for x in input().split()]
    workers    = input()
    even_cnt   = workers.count("E")
    odd_cnt    = n - even_cnt
    done = 0
    month = 0
    completed = False
    for i in range(1, m+1):
        if month == 0:
            can_use = min(k, min(x, odd_cnt))
            done += can_use
            odd_cnt -= can_use
            month = 1
        else:
            can_use = min(k, min(x, even_cnt))
            done += can_use
            even_cnt -= can_use
            month = 0
        if done >= n:
                print("Yes")
                completed = True
                break
    if not completed:
        print("No")



