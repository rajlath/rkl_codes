'''
Nested Segments
Time limit: 1000 ms
Memory limit: 256 MB

You are given NN segments. For each segment ii you know two integers l_il
​i
​​  and r_ir
​i
​​ , representing the left and the right ends of the segment.

A segment ii is nested inside segment jj if l_j < l_il
​j
​​ <l
​i
​​  and r_i <r_jr
​i
​​ <r
​j
​​ . Find the number of segments that are nested inside at least one other segment.

Standard input
The first line contains a single integer NN.

Each of the next NN lines contains two integers l_il
​i
​​  and r_ir
​i
​​ .

Standard output
Print the number of nested segments on the first line.

Constraints and notes
2 \leq N \leq 1002≤N≤100
0 \leq l_i \leq r_i \leq 1000≤l
​i
​​ ≤r
​i
​​ ≤100
Input	Output	Explanation
4
0 5
2 6
3 4
0 7
2
Segments (3, 4)(3,4) and (2, 6)(2,6) are nested inside (0, 7)(0,7).

4
1 5
0 5
0 5
1 6
0

'''
segments = []
for _ in range(int(input())):
    s, e = [int(x) for x in input().split()]
    segments.append((s, e))
nested_segments = 0
for i in range(len(segments)):
    for j in range(len(segments)):
        if segments[j][0] < segments[i][0] and  segments[i][1] < segments[j][1]:
            nested_segments += 1
            break
print(nested_segments)
