'''
n = int(raw_input())
t = sorted( zip( map(int, raw_input().split()), range(1, n+1) ) )
for i in xrange(n/2):
        print t[i][1], t[n-i-1][1]
→Judgement Protocol
Test: #1, time: 46 ms., memory: 4532 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
6
1 5 7 4 4 3
Output
1 3
6 2
4 5
Answer
1 3
6 2
4 5
'''
n = int(input())
arr = [int(x) for x in input().split()]
t = zip(arr, range(1, n+1))
t = sorted(t)
for i in range(len(t)//2):
    print(t[i][1], t[n-i-1][1])