'''
5
0 0 0 0 2 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0
1 2 2 3 4 0 3 4 4 1 3 1 4 4 1 0 0 0 0 0 4 2 3 2 2 1
1 1 3 3 1 1 4 4 3 1 3 3 3 0 1 2 0 4 2 1 3 0 3 1 1 1
3 3 0 2 2 2 4 1 2 1 1 1 3 3 0 0 3 2 2 4 1 4 4 1 2 1
2 1 4 1 0 2 0 3 1 2 0 3 1 1 2 0 1 4 2 3 2 3 2 0 2 1

3 2 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

Answer is:

3

Example:

acacacbb
'''
for _ in range(int(input())):
    freq = [int(x) for x in input().split()]
    less_till_now = freq[0]
    superiors = 0
    for i in range(26):
        if freq[i] > 0 and less_till_now > 0:
            if less_till_now > (freq[i]+1):
                curr = freq[i]
                less_till_now -= (curr + 1)
                superiors += curr
            else:
                curr = less_till_now - 1
                superiors += curr
                less_till_now = curr - 1
        else:
            less_till_now += freq[i]
    front = superiors

    less_till_now = sum(freq)
    superiors = 0
    for i in range(25, -1, -1):
        if freq[i] > 0 and less_till_now > 0:
            if less_till_now > freq[i]:
                curr = freq[i]
                less_till_now -= (curr + 1)
                superiors += curr
            else:
                curr = less_till_now - 1
                superiors += curr
                less_till_now = freq[i] - curr
        else:
            less_till_now += freq[i]
    back = (superiors)

    print(front, back)









