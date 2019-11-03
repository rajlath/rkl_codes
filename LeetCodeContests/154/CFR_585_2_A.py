team_a1 = int(input())
team_a2 = int(input())
yellow_a1 = int(input())
yellow_a2 = int(input())
total_yellow = int(input())
mins = max(0, total_yellow - team_a1 * ( yellow_a1 - 1) - team_a2 * (yellow_a2 - 1))
if yellow_a1 > yellow_a2:
    yellow_a1 , yellow_a2 = yellow_a2, yellow_a1
    team_a1, team_a2 = team_a2, team_a1
maxs = min(total_yellow // yellow_a1, team_a1)
total_yellow -= maxs * yellow_a1
maxs += min(total_yellow // yellow_a2, team_a2)
print(mins, maxs)