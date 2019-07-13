lens = int(input())
inss = input()
outs = input()
ans = lens
for i in range(lens):
    if outs.startswith(inss[i:]):
        ans = i
        break
print(ans)        
