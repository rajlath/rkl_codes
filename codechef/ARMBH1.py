nb_test = int(input())
for _ in  range(nb_test):
    salary , days = [int(x) for x in input().split()]
    due = 0
    current = salary
    while current < days:
        due += current
        current += salary
    print(due)
