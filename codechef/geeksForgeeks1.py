def sumOfDigits(n):
    return sum([int(x) for x in str(n)])
    sums = 0
    while n > 0:
        sums +=  n%10
        n //= 10
    return sums
def compute(n):
    answer = [0] * 100
    pos = 0
    for i in range(101):
        valueOnLeft = abs(n - i) +  sumOfDigits(abs(n - i))
        valueOnRight = (n + i) + sumOfDigits(n + i)
        if (valueOnRight == n):
            answer[pos] = (n + i)
            pos +=1
        if (valueOnLeft == n):
            answer[pos] = abs(n - i)
            pos += 1
    for i in range(pos+1):
        print(answer[i])

compute(100)



