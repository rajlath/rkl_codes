R=lambda:[int(x) for x in input().split()]
nb_problems, score_factor = R()
scores = R()
times= R()
def calc_score(u,v):
    x,y=0,0
    for i in range(nb_problems):
        y+=v[i]
        x+=max(0,u[i]-y*score_factor)
    return x
limak = calc_score(scores, times)
radew = calc_score(scores[::-1], times[::-1])
if limak == radew:
    print("Tie")
else:
    if limak > radew:
        print("Limak")
    else:
        print("Radewoosh")

