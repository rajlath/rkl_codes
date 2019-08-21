for _ in range(int(input())):
    curr = input()
    lens = len(curr)
    mids = lens // 2

    # if all the digits are 9
    if curr.count("9") == lens:
        print("1" + "0" * len(curr) + "1")
    else:
         if lens % 2 == 0:
             if curr[:mids][::-1] <= curr[mids:]:
                 cur = int(curr[:mids]) + 1
                 curr = str(cur)
             else:
                 curr = curr[:mids]
             print(curr + curr[::-1])
         else:
             if curr[:mids][::-1] <= curr[mids + 1:]:
                 cur = int(curr[:mids + 1]) + 1
                 curr= str(cur)
             else:
                 curr = curr[:mids + 1]
             print(curr + curr[:-1][::-1])



