import random

ages = [random.randint(1, 100) for x in range(100)]
max_age = max(ages)
age_count = {}
set_ages  = set()
for i in ages:
    age_count[i]  = age_count.get(i, 0) + 1
    set_ages.add(i)
rets = []
for j in set_ages:
    count = age_count[j]
    while count:
        rets.append(j)
        count -= 1
print(rets)


