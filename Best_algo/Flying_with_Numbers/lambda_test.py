from collections import defaultdict

minus_one_dict = defaultdict(lambda:(0,0))
for i in range(1, 10):
    minus_one_dict[i] = 5
print(minus_one_dict[12])
print(minus_one_dict)