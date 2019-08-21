R = lambda :[int(x) for x in input().split()]
nb_pages = int(input())
days = R()
idx = 0
while nb_pages > 0:
    nb_pages -= days[idx % 7]
    idx += 1
idx -= 1
print(idx % 7 + 1)    
