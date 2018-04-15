pair_val = {"00":0, "01": 1, "10": 2, "11": 3}
for _ in range(int(input())):
    ins = bin(int(input()))[2:]
    print(ins)
    ans = 0
    for i in range(len(ins)):
        for j in range(i+1, len(ins)):
            a = ins[i]+ins[j]
            ans += pair_val[a]
    print(ans)
