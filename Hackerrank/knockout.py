'''
18
41
18467
6334
26500
19169
15724
11478
29358
26962
24464
5705
28145
23281
16827
9961
491
2995
11942


40
18466
6333
26499
19168
15723
11477
29357
26961
24463
5704
28144
23280
16826
9960
490
2994
11941
4826
5435
32390
14603
3901
152
'''
for _ in range(int(input())):
    n = int(input())
    matches = 0
    while n > 2:
        matches +=  (n//2)
        n += n % 2
        n -= n // 2
        #print(matches, n)
    print(matches+1)
