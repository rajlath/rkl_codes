import re
nums = re.compile(r'\d+')
name = re.compile(r'(?<=\s)[a-z]+')
signature = { 'children': 0 , 'cats':  0, 'samoyeds': 0, 'pomeranians': 0, 'akitas': 0,'vizslas': 0, 'goldfish': 0, 'trees': 0, 'cars': 0, 'perfumes': 0,}

with open(r'E:\rkl_codes\AdventOfCodes\2015\day_16\input.txt') as f:
    for line in f:
        vals, names = [int(x) for x in nums.findall(line)], name.findall(line)
        sue_number = vals.pop(0)
        if(all(x == y for x, y in zip(map(signature.get, names), vals))):
            print(sue_number)
