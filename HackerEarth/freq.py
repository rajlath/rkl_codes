from collections import Counter
for _ in range(int(input())):
    given = Counter(input())
    for i in range(10):
        curr = 0
        if str(i) in given:
            curr = given[str(i)]
        print(curr, end=" ")    
