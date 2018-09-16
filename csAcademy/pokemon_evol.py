'''
Pokémon Evolution
Time limit: 1000 ms
Memory limit: 128 MB

You have recently caught NN Pokémon and you also have MM Pokémon candy bars. You can evolve any of your Pokémon by paying XX candy bars. Alternatively, you can sell any of your Pokémon for a price of YY candy bars. You cannot sell an evolved Pokémon.

Compute the maximum number of Pokémon you can evolve.

Standard input
The first line contains 44 integers N\ M\ X\ YN M X Y.

Standard output
The output should contain a single integer representing the maximum number of Pokémon you can evolve.

Constraints and notes
1 \leq N, M, X, Y \leq 10^91≤N,M,X,Y≤10
​9
​​
Input	Output	Explanation
5 10 2 1
5
You can evolve all the Pokémon if you use all the available candy.

3 10 4 2
2
You can evolve 22 Pokémon using the initial candy. Selling one Pokémon would result in a total of 10+2=1210+2=12 candy bars. This is enough to evolve 33 Pokémon, but you wouldn't have 33 Pokémon left to evolve.

10 3 1 1
6

'''
N, M, X, Y = [int(x) for x in input().split()]
left  = 0
right = N
while left != right:
    mid = (left + right+1 ) // 2
    if (M + (N-mid)*Y) >= mid * X:
        left = mid
    else:
        right = mid - 1
    #print(left, right)
print(left)