'''
Maximize Profit
Time limit: 1000 ms
Memory limit: 256 MB

You have an initial amount of money SS. There are QQ deals you can make to increase your sum. Each deal ii will either add a constant number KK, or it can increase your current amount by a percentage P_iP
​i
​​ .

You can apply the deals in any order, and for each of them you can choose wether it will add a constant value or a percentage. Maximize the final value of SS.

Standard input
The first line contains three integers SS, QQ and KK.

The second line contains QQ integers, the elements of PP.

Standard output
Print the answer on the first line.

Constraints and notes
0 \le S \leq 10^70≤S≤10
​7
​​
1 \le Q \le 501≤Q≤50
0 \leq K \leq 10^50≤K≤10
​5
​​
0 \leq P_i \leq 100 0≤P
​i
​​ ≤100
The answer is guaranteed to be at most 10^910
​9
​​  and will be evaluated with an absolute or relative precision of 10^{-6}10
​−6
​​
Input	Output	Explanation
100 3 20
10 50 30
234.00000000000
Use the first deal to increase the sum by 2020 having 120120

Use the third deal to increase the sum by 30\%30% having 156156

Use the second deal to increase the sum by 50\%50% finishing with 234234

20 2 30
100 100
100.00000000000
First deal, add 3030, resulting 5050

Second deal, add 100\%100%, resulting 100100

100 5 100
63 17 23 41 29
919.32000000000
Use deals 2, 32,3 and 55 to add 100100, resulting 400400

Use the forth deal to add 41\%41% resulting 564564

Use the first deal to add 62\%62% resulting 919,32919,32
'''
def get_pc_added(amt, perc):
    return amt * (perc + 100 /100) / 100
p, q, k = [int(x) for x in input().split()]
pc  = sorted([int(x) for x in input().split()])
maxp = p
for i in range(q):
    for j in range(len(pc)):
        p =(max(get_pc_added(p, pc[j]), p + k))
        print(p)

print(p)

