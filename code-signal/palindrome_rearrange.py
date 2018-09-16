from collections import Counter
def palindromeRearranging(inputString):
    isc = Counter(inputString)
    ones = 0
    for i in isc:
        if isc[i]%2 == 1:
            ones += 1
            if ones > 1: return False
        elif isc[i] %2 != 0:
            return False
    return True