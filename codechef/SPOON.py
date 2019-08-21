def has_spoon(grids):
    for i in grids:
        if 'spoon' in ''.join(i):
            return True
    for i in list(zip(*grids)):
        if 'spoon' in ''.join(i):
            return True
    return False    
for _ in range(int(input())):
    rows, cols = [int(x) for x in input().split()]
    grid = []
    for _ in range(rows):
        grid.append([x.lower() for x in input()])
    print(["There is indeed no spoon!","There is a spoon!"][has_spoon(grid)])
    
        