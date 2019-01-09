nb_test = int(input())
for _ in range(nb_test):
    nb_student = int(input())
    has_seen = [int(x) for x in input().split()]
    passed = max(has_seen)
    failed = nb_student - passed
    if failed == has_seen.count(passed):
        print(nb_student - passed)
    else:
        print(-1)
