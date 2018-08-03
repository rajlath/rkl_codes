'''
Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6
'''
#not working
noe, ratio = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
count = 0
for j in range(1, noe - 1):
    i = j - 1
    k = j + 1
    while i >= 0 and k < noe:
        if (arr[j] == (arr[i] * ratio)) and (arr[k] == (arr[j] * ratio))
            count += 1
            k += 1
            j -= 1
        elif arr[j] * ratio < arr[k]:
            k += 1
        else: i -= 1
print(count)
