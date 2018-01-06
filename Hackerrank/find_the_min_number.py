'''
Sample Input 1

4
Sample Output 1

min(int, min(int, min(int, int)))
'''
s = "min(int, int)"
i = int(input())
for i in range(2, i):
    s = "min(int,"+ s +")"
print(s)