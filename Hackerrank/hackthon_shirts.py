'''
Sample Input 0
2
5
2 3 6 9 13
4
3 7
4 8
14 16
10 13
2
3 2
2
3 4
4 5
Sample Output 0

3
1
'''
for _ in xrange(eval(raw_input())):
    needed = set()
    sizes  = set()
    #mins   = int(10e9 + 10)
    #maxs   = -(mins)

    nop = eval(raw_input())
    needed = set([int(x) for x in raw_input().split()])
    query = int(input())
    for  _ in range(query):
        b, e = [int(x) for x in raw_input().split()]
        #mins = min(mins, min(b, d))
        #maxs =
        sizes.update(range(b, e+1))
    print(len(sizes & needed))



