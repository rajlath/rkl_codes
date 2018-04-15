mods = int(10e9) + 7
def calc_values(k,prev,indx):
    return prev * k + 2

vals = [1]
prev = 0
k = 5
print(mods)
for i in range(1,20):
    nexts  = (calc_values(k,vals[-1],i+1))%mods
    vals.append(nexts)
print(vals)

counts = []
for i in range(1, 20):
    counts.append( (k ** i)%mods)
print(counts)

last = k
while True:






