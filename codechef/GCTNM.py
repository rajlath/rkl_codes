actual = "government college of engineering & textile technology berhampore"
actual = actual.lower().split(" ")
nots = int(input())
for _ in range(nots):
    entered = [x.lower() for x in input().split(" ")]
    ans = "accept"
    for i in range(len(entered)):
        ori = actual[i]
        cop = entered[i]
        diff = sum([1 if a != b else 0 for a, b in zip(ori,cop)])
        if diff * 2 > len(ori):
            ans = "reject"
            break
    print(ans)

