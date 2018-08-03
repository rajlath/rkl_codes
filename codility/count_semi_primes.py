def solution(N, P, Q):
    '''
    N int : limit from 1 to N
    p int : range start
    Q int : range end inclusive
    return ans : int - number of semiprimes in the range P .. Q
    '''
    #generate prime sieve upto N+1
    primes = [False, False] + [True] * (N - 1)
    prime_count = 0
    for i in range(2, N+1):
        if primes[i]:
            prime_count += 1
            for j in range(i*2, N+1, i):
                primes[j] = False

    #generate semi primes seive upto N+1
    semi = set()
    i = 2
    while i * i <= N:
        if primes[i]:
            for j in range(i*i, N+1, i):
                if j % i == 0 and primes[j//i] == True:
                    semi.add(j)
        i += 1


    #generate semi counts
    semi_count = [0,0,0,0,1]
    for i in range(5, max(Q)+1):
        semi_count.append(semi_count[-1] + int(i in semi))


    #genrerate solution
    answer = []
    for i in range(len(Q)):
        answer.append(semi_count[Q[i]] - semi_count[P[i] - 1])

    return answer

print(solution(26,[1, 4, 16], [26,10,20]))


