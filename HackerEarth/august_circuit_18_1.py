from collections import Counter
lens = int(input())
arr  = Counter(input())
print(lens - arr.most_common()[0][1])