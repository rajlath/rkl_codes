'''
Lucky Days
Time limit: 1000 ms
Memory limit: 256 MB

Alex has started playing poker and he discovered he is so good, that everyday he wins a certain amount of money. You are given an array AA of NN elements, where A_iA
​i
​​  is the amount he won during the i^{th}i
​th
​​  day.

Alex calls a day lucky if he wins strictly more money than in any of the previous days. Note that by this definition the first day is always lucky.

Find the total number of lucky days.

Standard input
The first line contains a single integer NN.

The second line contains NN positive integers, representing the elements of AA.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq N \leq 1001≤N≤100
1 \leq A_i \leq 1001≤A
​i
​​ ≤100
Input	Output	Explanation
7
1 5 2 3 4 5 7
3
Days 11, 22 and 77 are lucky.

5
1 1 3 3 3
2
Only days 11 and 33 are lucky. Notice the amount of money won in a lucky day should be strictly greater than those from the previous days.
'''
days = int(input())
vals = [int(x) for x in input().split()]
max_till_now = 0
all_max = []
for i,v in enumerate(vals):
    if v > max_till_now:
        all_max.append(i+1)
        max_till_now = v
print(len(all_max))
