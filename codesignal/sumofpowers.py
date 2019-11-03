def sumOfPowers(n, divisor):
    s=0
    for i in range(1, n+1):
        k = 0
        while (i%pow(divisor,k)==0):k+=1
        s += (k - 1)
    return s

print(sumOfPowers(6,2))
