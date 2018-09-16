'''
Poisoned Food
Time limit: 1000 ms
Memory limit: 256 MB

Alex went to a party where there are NN types of food. For each type you know the total number of portions and the number of portions that have been poisoned. Unfortunately, you don't know which portions are safe and which are poisoned.

The rules of the house say you have to eat, so Alex wants to minimize the risk of eating a poisoned portion. Find the type of food that is the safest to eat, if Alex chooses a random portion of that type.

Standard input
The first line contains a single integer NN.

Each of the next NN lines contains 22 integers t_it
​i
​​  and p_ip
​i
​​ , representing the total number of portions and the number of portions that have been poisoned for the i^{th}i
​th
​​  type of food.

Standard output
Print the index of the safest type of food on the first line. If the solution is not unique, print the smallest value.

Constraints and notes
1 \leq N \leq 1001≤N≤100
1 \leq p_i \leq t_i \leq 1001≤p
​i
​​ ≤t
​i
​​ ≤100
Input	Output	Explanation
3
2 1
3 2
4 2
1
The 1^{st}1
​st
​​  and the 3^{rd}3
​rd
​​  types of food are the safest, with a probability of 50\%50% of eating a poisoned portion.

5
10 6
20 12
50 40
9 5
18 10
4
The 4^{th}4
​th
​​  and the 5^{th}5
​th
​​  types of food are the safest.
'''
safest = 1
safe_pc= 100
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    pc = (100 * (b / a) /100)
    #print(pc)
    if pc < safe_pc:
        safest = i + 1
        safe_pc = pc
print(safest)


