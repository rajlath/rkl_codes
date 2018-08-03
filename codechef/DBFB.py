'''
Example Input
1
3 3
1 2 3
4 5 6
Example Output
63
'''
mods = int(10e9 + 7)
for i in range(int(input())):
    first, second = [int(x) for x in input().split()]
    firarr = [int(x) for x in input().split()]
    secarr = [int(x) for x in input().split()]
    sums = sum(secarr[:first]) % mods
    result = 0
    for i in range(first):
        mid = sums + (firarr[i] * second)%mods
        result += mid
        result%=mods
    print(result%mods)