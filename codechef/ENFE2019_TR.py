MAX = 10 ** 9
def findStates(position):
    positions = [0,0,1,1,1,0,1,0,1]
    for i in range(8, MAX + 1):
        if not(position[i - 2]) or not(position[i - 3]) or not(position[i - 4]):
            position[i] = 1
        else:
            position[i] = 0

position = [0] * (MAX + 1)
findStates(position)
print(position[:20])
N = 123
if position[N] == 1:
    print(1)
else:
    print(2)


