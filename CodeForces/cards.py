'''
3
4 5 7
output
Conan
input
2
1 1
output
Agasa
'''
n = int(input())
arr = sorted([int(x) for x in input().split()], reverse=True)
maxs = arr[0]
cnt = 0
for i in range(1, n):
    if arr[i] != arr[i-1]:
        break
    else:
        cnt += 1
if cnt == 0 or cnt % 2 == 0:
    print('Conan')
else:print('Agasa')
