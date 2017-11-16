
noOfBldg, noOfItem, kFactor  = [int(x) for x in input().strip().split()]
bldgO     = [int(x) for x in input().strip().split()]
bldg      = [i for i, v in enumerate(bldgO) if v == 1]

if len(bldg) < noOfItem : print(-1)
elif len(bldg) == 1: print(bldg[0])
else:
	final_ans, ans = 0, 0

	for i in range(noOfItem):
		if i == 0:
			ans += bldg[i]
		else:
			ans += (bldg[i] - bldg[i-1])*kFactor*i
	final_ans = ans


	for i in range(noOfItem, len(bldg) ):
		decr   = (bldg[i-1] - bldg[i - noOfItem]) * kFactor
		left_inc=bldg[i-noOfItem+1] - bldg[i-noOfItem]
		right_inc = (bldg[i] - bldg[i-1] ) * (noOfItem-1)*kFactor
		ans = ans - decr + left_inc + right_inc	
		final_ans = min(final_ans, ans)

print(final_ans)





