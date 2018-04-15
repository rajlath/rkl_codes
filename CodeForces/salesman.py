'''
input
111111011
2
output
169
'''
print(bin(84)[2:])
ins = input()
k   = int(input())
sets = ins.count("1")
start = int(ins, 2)
print(start, sets)
cnt = 0

for i in range(1, start+1):
    x = bin(i)[2:]
    if x.count("1") == 5:
        cnt += 1
        print(x, int(x,2))
print(cnt)




