'''
you can perfectly predict the price of a certain stock for the next N days.
you would like to profit on this knowledge, but only want to transact one share of stock per day.
That is, each day you will either buy one share, sell one share, or do nothing.
Initially you own zero shares, and you cannot sell shares when you don't own any.
At the end of the N days you would like to again own zero shares, but want to have as much money as possible.

Input
Input begins with an integer N (2 ≤ N ≤ 3·10^5), the number of days.

Following this is a line with exactly N integers p1, p2, ..., pN (1 ≤ pi ≤ 10^6).
The price of one share of stock on the i-th day is given by pi.

Output
Print the maximum amount of money you can end up with at the end of N days.

Examples
input
9
10 5 4 7 9 12 6 2 10
output
20
input
20
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4
output
41
Note
In the first example, buy a share at 5, buy another at 4, sell one at 9 and another at 12.
Then buy at 2 and sell at 10.
The total profit is  - 5 - 4 + 9 + 12 - 2 + 10 = 20.
'''

from sys import stdin
from itertools import repeat
from heapq import heappush, heappushpop
def main():
    n = int(stdin.readline())
    a = map(int, stdin.readline().split(), repeat(10, n))    
    q = []
    ans = 0
    for x in a:
        if q and x - q[0] > 0:
            ans += x - q[0]
            heappushpop(q, x)
            heappush(q, x)
        else:
            heappush(q, x)
        #print(q, ans)    
    print(ans)
main()
