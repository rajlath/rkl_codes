from string import  ascii_lowercase as lc
lens = int(input())
counts = [{x:0 for x in lc} for _ in range(lens)]

for i in range(lens):
    current = input()
    for ch in current:
        counts[i][ch] += 1
result = counts[0]
print(counts[1]['h'])

for i in range(1, lens):
    for j in lc:
        result[j] = min(result[j], counts[i][j])
answer = ''
for x, v in result.items():
    if v > 0:
        answer += x * v
print(answer)        
