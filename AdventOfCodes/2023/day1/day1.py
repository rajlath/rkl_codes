import re 

nums = ['one', 'two','three','four','five','six','seven','eight','nine']
numd = ['1','2','3','4','5','6','7','8','9']

def getNumber(sts)   :
    if sts in nums:
        return int(nums.index(sts) + 1)
    else:
        return int(numd.index(sts) + 1)
    
    
with open('input.txt') as f:
    lines = f.read().splitlines()

part_1 = 0
for line in lines:
    alls = "".join(re.findall(r"\d", line))
    curr = int(alls[0] + alls[-1])
    part_1 += curr
    print(curr, part_1)
print(part_1) 

part_2 = 0
for line in lines:
    alls = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    print(alls[0], alls[-1])
    sums = str(getNumber(alls[0])) + str(getNumber(alls[-1]))
    print(sums)
    part_2 += int(sums)
    
print(part_2)    
    