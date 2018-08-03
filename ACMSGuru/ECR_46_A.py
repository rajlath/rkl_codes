'''
input
3
XS
XS
M
XL
S
XS
output
2
'''
sizes = ["M", "S", "L", "XS", "XL", "XXS", "XXL", "XXXS", "XXXL"]
nos = int(input())
last_year = []
curr_year = []
needed = 0
for i in range(nos):
    last_year.append(input())
for i in range(nos):
    curr_year.append(input())
for i in last_year:
    if i in curr_year:
        curr_year.pop(curr_year.index(i))
print(len(curr_year))

'''
for x in last_year:
    if x in curr_year:
        curr_year.pop(curr_year.index(x))
    else:
        for indx , v in enumerate(curr_year):
            if len(x) ==1 and len(v) == 1 and v not in last_year:
                needed += 1
                curr_year.pop(indx)
            elif len(x) == 2 and len(v) == 2 and v not in last_year:
                needed += 1
                curr_year.pop(indx)
            elif len(x) == 3 and len(v) == 3 and v not in last_year:
                needed  += 1
                curr_year.pop(indx)
            elif len(x)==4 and len(v) == 4 and v not in last_year:
                needed += 1
                curr_year.pop(indx)

print(curr_year, last_year)
print(needed)
'''


