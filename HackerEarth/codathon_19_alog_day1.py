nb_test = int(input())
for i in range(nb_test):
    positions = [0]
    reach = int(input())
    steps = [int(x) for x in input().split()]
    for i in range(3):
        curr = steps[i]
        updt = []
        for j in range(len(positions)):
            updt.append(positions[j] + curr)
            updt.append(positions[j] - curr)
        positions = updt[:]
    print(["LOSE", "WIN"][reach in positions])