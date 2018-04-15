'''
4 1 1
1 1 2 1
Output
2
Answer
2
Checker Log
ok answer is '2'
'''
group_cnt, ones, twos = [int(x) for x in input().split()]
entries = [int(x) for x in input().split()]
one_one = 0
denied  = 0
for i in entries:
    if i == 1:
        if ones:ones-=1
        elif twos:
            twos -= 1
            one_one += 1
        elif one_one: one_one -= 1
        else: denied += 1
    else:
        if twos: twos -= 1
        else:denied += 2
print(denied)




