for _ in range(int(input())):
    ins = int(input())
    cnt = 0
    while ins > 1:
        ins = [ins//2, 3*ins+1][ins%2]
        cnt += 1
    print(cnt)     
        
