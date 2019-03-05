def get_score(s, t, ls, lt):
    if ls == lt:
        diff = sum([1 for x, y in zip(s, t) if x == y])
        return diff <= 1
    if ls + 1 == lt:
        diff = -1
        for i in range(ls):
            if s[i] != t[i]:
                diff = i
                break
        if diff == -1:return True
        for i in range(diff, ls):
            if s[i] != t[i+1]:
                return False
        return True
    if ls - 1 == lt:
        diff = -1
        for i in range(lt):
            if s[i] != t[i]:
                diff = i
                break
        if diff == -1:return True
        for i in range(diff, lt):
            if s[i+1] != t[i]:
                return False
        return True    
                
    
        
N = int(input())
pattern = input()
result = 0
for i in range(N):
    curr = input()
    lens = len(pattern)
    lent = len(curr)
    if abs(lens - lent) > 1:continue
    if pattern == curr:continue
    result += get_score(pattern, curr, lens, lent)
       
print(result)    
    
        