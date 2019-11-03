lens = int(input())
inss = input()
ans  = []
ans.extend(["1"] * inss.count("n"))
ans.extend(["0"] * inss.count("z"))
print(*ans)