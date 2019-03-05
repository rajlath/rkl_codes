can_use = int(input())
nb_months = int(input())
has = can_use
for _ in range(nb_months):
    has += can_use - int(input())
print(has)
