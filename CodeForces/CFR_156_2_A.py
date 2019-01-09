nb_exer = int(input())
to_do   = [int(x) for x in input().split()]
done = [0, 0, 0]
for i in range(nb_exer):
    done[i%3] += to_do[i]
print(["chest", "biceps", "back"][done.index(max(done))])


