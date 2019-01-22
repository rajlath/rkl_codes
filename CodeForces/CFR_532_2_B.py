from collections import defaultdict
problem_in_round, problems = [int(x) for x in input().split()]
difficulties = [int(x) for x in input().split()]
teams  = defaultdict(list)
counts = defaultdict(int)
for i in difficulties:
    counts[i]+=1
    teams[counts[i]].append(i)
    if len(teams[counts[i]]) == problem_in_round:
        print("1", end='')
    else:
        print("0", end='')
    
