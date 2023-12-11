seqs = [[int(x) for x in line.strip().split()] for line in open("day9.txt").readlines()]

def extrapolate(array): 
    if all(x == 0 for x in array):
        return 0
    
    diffs = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate(diffs)
    return array[-1] + diff

def extrapolate2(array):
    if all(x == 0 for x in array):
        return 0

    diffs = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate2(diffs)
    return array[0] - diff

    

print(sum([extrapolate(x) for x in seqs]))  #1584748274
print(sum(extrapolate2(x) for x in seqs))   #1026
    
    


