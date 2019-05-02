import bisect
nb_test = int(input())
for _ in range(nb_test):
	nb_soldier, nb_query = [int(x) for x in input().split()]
	print(nb_soldier, nb_soldier)
	heights = [0] + [int(x) for x in input().split()]
	living  = [0] * (nb_soldier + 1)
	answer  = []
	for _ in range(nb_query):
		index, limit = [int(x) for x in input().split()]
		living[index] = 1
		j = bisect.bisect(heights, limit)
		if j < nb_soldier + 1:
			while living[j]:
				j += 1
				if j == (nb_soldier + 1):
					answer.append(-1)
				else:
					answer.append(j)
		else:
			ans.append(-1)
	print(*answer)

					
					



