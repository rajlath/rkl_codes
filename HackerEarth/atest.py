n = 345340
sums = (n * (n+1))//2
print(sums)   #59630030470 -    390548434
print(59630030470)

offs = 9
for i in range(1, 345340//10):
    offs += 9*i
print(offs)

#1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 12,22,
'''
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1,                        9   9   10
11, 12, 13, 14, 15, 16, 17, 18, 19, 2,                 18   18  20    9
12, 22, 23, 24, 25, 26, 27, 28, 29, 3,  9              27   36  30    18
13, 23, 33, 34, 35, 36, 37, 38, 39, 4,  18 9           36   63  40    27
14, 24, 34, 44, 45, 46, 47, 48, 49, 5,  27 18 9        45   99  50    36
15, 25, 35, 45, 55, 56, 57, 58, 59, 6,  36 27 18 9     54   144 60    45
16, 26, 36, 46, 56, 66, 67, 68, 69, 7,  45 36 27 18 9  63   198 70    54
17, 27, 37, 47, 57, 67, 77, 78, 79, 8,  54 45 36 27 18 9 72
9 18 9
'''

