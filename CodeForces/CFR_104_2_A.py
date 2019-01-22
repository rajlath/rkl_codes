lens = int(input())
ins  = input()
ans  = "NO"
if len(ins.replace("4","").replace("7",'')) == 0:
    if sum(map(int, ins[:lens//2])) == sum(map(int,ins[lens//2:])) :
        ans = "YES"
print(ans)