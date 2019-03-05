
def digsum(n):
    return sum([int(x) for x in str(n)])
n = int(input())
while True:
    n1 = digsum(n)
    if n % n1 == 0:break
    n +=1
print(n)
