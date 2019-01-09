nb_points, nb_segments = [int(x) for x in input().split()]
zone_lens = [int(x) for x in input().split()]
meet_at = nb_points / 2
sums = 0
for i in range(nb_points):
    sums += zone_lens[i]
    if sums == meet_at:
        print(-1)
        break
    if sums < meet_at:
        print(i + 1)
        break
    print(sums, meet_at)
    
