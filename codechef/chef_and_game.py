'''
2
2
1 2
5
7 4 3 2 6
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    even = sum([1 for x in arr if x%2==0])
    odd = noe - even
    answer = (odd * (odd - 1) + even * (even - 1)) // 2
    print(noe - answer)


