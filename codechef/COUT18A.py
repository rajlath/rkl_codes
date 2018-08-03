'''
Problem Statement
You are given with N segments on x-axis in the form of their endpoints.
You have to output the number of distinct integral points that are covered by the
line segments.

INPUT
First line contains the no. of test cases T.
First line of each test case contains the number N, then N line follows containing two
integers A and B, the endpoints of the ith segment.

OUTPUT
Output a single integer according to the above problem.

Input

1
2
1 3
5 8

Output

7
'''
for _ in range(int(input())):
    nos = int(input())
    segments = []
    for i in range(nos):
        segments.append([int(x) for x in input().split()])
    segments = sorted(segments, key = lambda x:x[0])
    begin = segments[0][0]
    ends  = segments[0][1]
    total = ends - begin + 1
    for i  in range(1, nos):
        curr_begin = segments[i][0]
        curr_end   = segments[i][1]
        if curr_begin > ends:
            ends = curr_end
            begin= curr_begin
            total += curr_end - curr_begin + 1
        elif curr_begin <= ends and curr_end >= last:
            total += curr_end - last
            last = curr_end
            begin= curr_begin
        elif last > curr_end:
            begin = curr_begin
    print(total)

