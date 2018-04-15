'''
5
Arber 5 11
Ardit 4 12
Marsed 3 5
Gledi 2 2
Ana 1 6
'''
winner = ''
max_solved = 0
for _ in range(int(input())):
    name, dec, jan = [x for x in input().split()]
    score = int(jan) - int(dec)
    if score > max_solved:
        winner = name
        max_solved = score
print(winner, max_solved)
