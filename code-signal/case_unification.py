def caseUnification(inputString):
    lower = sum([1 for x in inputString if x.islower()])
    upper = len(inputString) - lower
    if lower > upper:
        return inputString.lower()
    else:
        return inputString.upper()

print(caseUnification("ABabc"))
caseUnification = lambda I: sum(a>'Z' for a in I)>len(I)/2 and I.lower() or I.upper()
