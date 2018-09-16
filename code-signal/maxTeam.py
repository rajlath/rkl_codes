players = [[88, 47, 42, 21],
          [40, 76, 21, 22],
          [45, 92, 1, 1],
          [22, 23, 10, 11],
          [1, 100, 1, 0],
          [40, 70, 90, 80],
          [40, 12, 45, 12],
          [40, 80, 81, 80],
          [40, 50, 60, 70],
          [0, 0, 0, 99],
          [12, 54, 44, 55]]

'''
he best team could be chosen as follows:

goalkeeper: player 0 (88)
defenders: players 1, 2, 3, and 4 (76 + 92 + 23 + 100 = 291)
midfielders: players 5, 6, and 7 (90 + 45 + 81 = 216)
forwards: players 8, 9, and 10 (70 + 99 + 55 = 224)
For a grand total of 88 + 291 + 216 + 224 = 819
'''
def theBestTeam(players):
    positions = (players)
    max_score = 0
    for i in range(11):
        if i == 0:
            max_score += max(positions[0])
        if i in range(1,5):
            max_score += positions[i][1]
        if i in range(5,8):
            max_score += positions[i][2]
        else:
            max_score += positions[i][3]
        print(max_score)
    return max_score






print(theBestTeam(players))


