'''
Anomalies
Time limit: 1000 ms
Memory limit: 256 MB

You are given an array AA of NN integers. An anomaly is a number for which the absolute difference between it and all the other numbers in the array is greater than KK. Find the number of anomalies.

Standard input
The first line contains two integers NN and KK.

The second line contains NN integers, representing the AA array.

Standard output
The first line should contain the number of anomalies.

Constraints and notes
1 \leq N, K \leq 1001≤N,K≤100
1 \leq A_i \leq 10001≤A
​i
​​ ≤1000, for any 1 \leq i \leq N1≤i≤N
Input	Output
3 1
1 3 5
3
3 5
7 1 8
1
5 1
1 2 2 2 2
0
'''
n, k = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
anam = 0
for i in range(n):
    valid = True
    for j in range(n):
        if i == j:continue
        if abs(arr[i] - arr[j]) <= k:
            valid = False
            break
    anam += valid


print(anam)

