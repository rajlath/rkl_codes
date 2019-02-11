nb_robots = int(input())
done = {}
robots = [input() for _ in range(nb_robots)]
for i in range(nb_robots):
    curr = ''
    for j in range(len(robots[i])):
        curr += robots[i][j]
        done[curr] = done.get(curr, 0) + 1
    print(done[robots[i]])
    print(done)

