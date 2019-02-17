N = 1000000
min_prime = [0] * N
i = 2
while i * i <=N:
    if min_prime[i] == 0:
        j = i * i
        while j <= N:
            if  min_prime[j] == 0:
                min_prime[j] = i
for i in range(2, N+1):
    if min_prime[i] == 0:
        min_prime[i] = i
count = [0] * (N+1)
for i in range(2, N+1):
    count[min_prime[i]] +=1

nb_test = int(input())
for _ in range(nb_test):
    print(min_prime[int(input())])