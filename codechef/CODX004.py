def sum_digits(s):
    return sum([int(x) for x in s])
ins = input().strip()
#difference = abs(int(ins[0]) + int(ins[1]) + int(ins[2]) - int(ins[3]) - int(ins[4]) - int(ins[5]))
difference = abs(sum_digits(ins[:3]) - sum_digits(ins[3:]))
if difference != 0:
    answer, mod = divmod(difference, 9)
    if mod > 0:
        answer += 1
    print(answer)
else:print(0)
