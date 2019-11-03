'''
Sample Input
2
900
1100

Sample Output

900.00
990.00
'''
for _ in range(int(input())):
    current = int(input())
    topay   = [current, (current * 90)//100][current > 1000 ]
    print("{0:.2f}".format(topay))
