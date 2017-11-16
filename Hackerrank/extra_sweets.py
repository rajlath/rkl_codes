'''
Sample Input 1

10 2
3 3
5 6
Sample Output 1

9
19
'''
bar_len, nos_student = [int(x) for x in input().split()]
got_l_r = False
ans = 0
for i in range(nos_student):
    l, r =  [int(x) for x in input().split()]
    ls-=1
    rs+=1
    le = 0 <= ls <= bar_len * l
    re = 0 <= rs <= bar_len * r

    if not got_l_r:
        
    print(r * (r + 1) - l * (l - 1)) / 2 + ls + rs)
    




