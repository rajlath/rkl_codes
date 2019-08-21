for _ in range(int(input())):
    lens = 4 * int(input())
    arrs = [int(x) for x in input().split()]
    def validate(arrs):
        arrs = sorted(arrs)
        for i in range(0, lens, 2):
            if arrs[i] != arrs[i+1]:
                return "NO"
        prod = arrs[0] * arrs[-1]
        for i in range(lens//2):
            if arrs[i] * arrs[-i-1] != prod:
                return "NO"
        return "YES"
    print(validate(arrs))        
