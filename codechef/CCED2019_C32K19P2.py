def calc_score(a, start_pos, end_pos, total_sum):
    left_sum = 0
    rite_sum = total_sum
    for split_pos in range(start_pos, end_pos):
        left_sum += a[split_pos]
        rite_sum -= a[split_pos]
        if left_sum > rite_sum : break
        if left_sum == rite_sum:
            cnt += 1
        return    calc_score(a, start_pos, split_pos, left_sum)
        return    calc_score(a, split_pos + 1, end_pos, rite_sum)


a = [1,2,3,4]
sums = sum(a)
print(calc_score(a, 0, len(a)-1, sums))