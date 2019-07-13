def QuestionsMarks(str):
    nums = [(int(x), i)  for i, x in enumerate(str) if x.isdigit()]
    counts = 0
    rets = True
    has10 = False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i][0] + nums[j][0] == 10:
                has10=True
                current = str[nums[i][1]:nums[j][1]]
                if current.count("?") >= 3 : continue
                else:
                    rets = False
                    break
    if not has10 : return False
    return rets



# keep this function call here
print( QuestionsMarks("acc?7??sss?3rr1??????5"))