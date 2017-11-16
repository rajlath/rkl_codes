import operator
scores = {}
for _ in range(int(input())):
    n, c = [x for x in input().split()]
    scores[n] = scores.get(n, int(c))
sscore = sorted(scores.items(),key=operator.itemgetter(1), reverse=True)   
for i in range(3)  :
    print(sscore[i][0])
