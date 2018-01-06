yellow, blue = [int(x) for x in input().split()]
a, b, c      = [int(x) for x in input().split()]
yellow_needed= (a*2 + b*1) - yellow
if yellow_needed < 0:
    yellow_needed = 0
blue_needed  = (b* 1 + 3 * c) - blue
if blue_needed < 0:
    blue_needed = 0

print(yellow_needed + blue_needed)
































