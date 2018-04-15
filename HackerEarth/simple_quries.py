'''
7
0110011
6
2 1 7
1 1
2 1 7
1 4
1 5
2 1 7

1
4
-1
'''

nos = int(input())
arr = list(input())
for _ in range(int(input())):
    qur = [x for x in input().split()]
    if len(qur) == 3:
        b,c = int(qur[1])-1, int(qur[2])-1
        try:
            print(arr[b:c+1].index("0") + 1)
        except ValueError:
            print(-1)
    else:
        indx = int(qur[1]) - 1
        arr[indx]= ["1", "0"][arr[indx]=="1"]








