'''
Sample Input:
1
2
5 2

Sample Output:
YES
'''
for _ in range(int(input())):
    bulk = int(input())
    qty  = [int(x) for x in input().split()]
    print(["NO", "YES"][sum(qty)%2==1])