def is_square_sum(n):
    i = 2
    while i * i <= n:
        cnt = 0
        if n % i == 0:
            while n%i==0:
                cnt +=1
                n //= i
            if i % 4 == 3 and cnt % 2 != 0:
                return False
        i+= 1
    return n%4 != 3

print(["NO", "YES"][is_square_sum(int(input()))])


