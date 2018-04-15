def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print (partial)
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        print(n, i)
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    subset_sum([2,3,5],8)