num = int(input())
count = 0
while num > 0:
	num -= int(max([x for x in str(num)]))
	count += 1
print(count)
