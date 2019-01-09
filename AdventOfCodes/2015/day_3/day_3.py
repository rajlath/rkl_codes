# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:11:46 2018

@author: rinfo
"""
line = open("input.txt").read().strip()
done = [(0,0)]
col = 0
row = 0
house = 1
'''
for i in line:
    if i == "^":
        col += 1
    elif i == ">":
        row +=1
    elif i == "<":
        row -= 1
    else:
        col -= 1
    curr = (col, row)
    if curr not in done:
        house += 1
        done.append((col, row))
print(house)        
'''
x = 0
y = 0
x2 = 0
y2 = 0
presents = {}
present_count = 1
presents[(x,y)] = presents.get((x,y), 0) + 1
presents[(x2,y2)] = presents.get((x2,y2), 0) + 1

turn = 0
for move in line:
    if turn == 0:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move =='<':
            x -= 1
        else:
            continue
        presents[(x,y)] = presents.get((x,y), 0) + 1
        turn = 1
    elif turn == 1:
        if move == '^':
            y2 += 1
        elif move == 'v':
            y2 -= 1
        elif move == '>':
            x2 += 1
        elif move =='<':
            x2 -= 1
        else:
            continue
        presents[(x2,y2)] = presents.get((x2,y2), 0) + 1
        turn = 0
    present_count += 1

print(present_count, "presents were given.")
print(len(presents), "houses received at least one present.")

        
    
        
        
    
    
