for _ in range(int(input())):
    bfh, bfm = [int(x) for x in input().split(":")]
    gfh, gfm = [int(x) for x in input().split(":")]
    home_dist = int(input())

    curr_diff = (bfh * 60 + bfm) - (gfh * 60 + gfm)
    if curr_diff == 2 * home_dist:
        print("{:.1f} {:.1f}".format(curr_diff + home_dist, curr_diff))
    elif curr_diff > 2 * home_dist:
        print("{:.1f} {:.1f}".format(curr_diff + home_dist, curr_diff))
    else:
        print("{:.1f} {:.1f}".format(curr_diff + home_dist, home_dist + curr_diff/2))


