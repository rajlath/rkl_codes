fibo = [0, 1]
for i in range(2, 26):
    fibo.append(fibo[i-1] + fibo[i-2])
n = int(input())
print(fibo[n])