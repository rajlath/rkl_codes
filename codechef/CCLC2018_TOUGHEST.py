lens = int(input())
def digsum(x):
    return sum([int(i) for i in str(x)])
print(sum([1 if digsum(x)%3==0 else 0 for x in [int(x) for x in input().split()]]))