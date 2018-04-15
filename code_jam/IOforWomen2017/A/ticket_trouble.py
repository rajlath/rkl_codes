'''
'''
in_file = open('A-small-practice.in', 'r')
ou_file = open('A-small-practice.ou', 'w')

case_cnt = int(in_file.readline().strip())
for case in range(case_cnt):
    frnds_cnt, row_cnt = map(int, in_file.readline().strip().split())
    seats = [[0 for x in range(2)] for y in range(row_cnt+1)]


    max_in_row = 0
    for i in range(frnds_cnt):
        cnt = 0
        occupied = [0] * (row_cnt+1)
        row, col = map(int, in_file.readline().strip().split())
        seats[i][0] = row
        seats[i][1] = col

        for seat in seats:
            if seat[0] == i and not occupied[seat[1]]:
                cnt += 1
                occupied[seat[1]] = True
            else:
                if seat[1] == i and not occupied[seat[0]]:
                    cnt += 1
                    occupied[seat[0]] = True
            max_in_row = max(max_in_row, cnt)
    ou_file.write("Case #{}: {}".format(case+1, max_in_row))
    ou_file.write("\n")



