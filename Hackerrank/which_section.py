for _ in range(int(input())):
    n, q, nos = [int(x) for x in input().split()]
    section_cnt=[int(x) for x in input().split()]
    start = 1
    sections = []
    for i in range(nos):
        sections.append([start, start+section_cnt[i] - 1])
        start += section_cnt[i]
    for i in range(nos):
        if sections[i][0] <= q <= sections[i][1]:
            print(i+1)
            break



