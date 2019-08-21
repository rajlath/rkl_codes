def sum_digits(n):
    sums = 0
    while n > 0:
        n, bal = divmod(n, 10)
        sums += bal
    return sums

given = int(input())
counts = 0
for i in range(given-120, given):
    curr = sum_digits(i)
    
    if  i > 0 and (i + curr + sum_digits(curr)) == given:
        counts += 1
print(counts)
