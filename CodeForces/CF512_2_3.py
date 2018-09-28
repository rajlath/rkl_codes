nb_digit = int(input())
digits   = [int(x) for x in input()]
sums     = sum(digits)
print(sums)
if sums%3 != 0:
    print("NO")
else:
    ans = "YES"
    seg_sum = sums // 3
    maxlens = nb_digit//3
    s_sum = 0
    d_cnt = 0
    d_done= 0
    for i in range(nb_digit):
        while d_cnt <= maxlens:
            s_sum += digits[i]
            d_cnt += 1
            if s_sum == seg_sum and d_cnt <= maxlens:
                print(i, s_sum)
                s_sum = 0
                d_cnt = 0
        else:
            ans = "NO"
            break
    print(ans)



