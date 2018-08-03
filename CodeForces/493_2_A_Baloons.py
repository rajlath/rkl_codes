nobp = int(input())
ballon_cnt = [int(x) for x in input().split()]
if nobp == 1 or len(ballon_cnt)==2 and len(set(ballon_cnt))==1:
    print(-1)
else:
    print(1)
    print( ballon_cnt.index(min(ballon_cnt)) + 1)
    




