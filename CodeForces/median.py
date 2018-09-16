def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.

noe, value = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
meds = median(arr)
nops = abs(meds - value)
arr[arr.index(meds)] = value
meds = median(arr)
nops += abs(meds - value)
print(nops)