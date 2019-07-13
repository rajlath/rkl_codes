class NBAFinals:
    def dubAgain(self, scores, team):
        raptor, warrior = 0, 0
        for i in range(len(scores)):
            score, teams =  scores[i], team[i]
            if teams == "R":
                if score == 0:
                    raptor += 1
                else:raptor += score
            else:
                if score == 0:
                    warrior += 4
                else:
                    warrior += score
        if warrior > raptor :return 1
        else:return 0

print(NBAFinals().dubAgain(	[2, 2, 3, 3, 2, 4, 2], "RRWWRWR"))

'''
class NBAFinals:
    def dubsAgain(self, scores, team):
        r, w = 0, 0
        for i in range(len(scores)):
            t, s = team[i], scores[i]
            print(t, s)
            if t == 'R':
                if s == 0:
                    r += 1
                else:
                    r += s
            else:
                if s == 0:
                    w += 4
                else:
                    w += s
        if w > r:
            return 1
        return 0
'''
