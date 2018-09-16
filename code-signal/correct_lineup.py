def correctLineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]

athletes =  [1, 2, 3, 4, 5, 6]
print(checkParticipants(athletes))


