from itertools import groupby
chain = ["9"]
for i in range(1, 21):
    chain.append("".join([str(len(list(g)))+k for k, g in groupby(chain[-1])]))
for _ in range(int(input())):
    print(chain[int(input())])

