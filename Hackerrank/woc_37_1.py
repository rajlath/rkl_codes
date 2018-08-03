

'''

def rounding(x):
    x = float(x)
    y = floor(x)
    if x - y >0.0:
        y += 1.0
    return y


def rounding(n):
    n = str(n).split(".")
    if len(n)==1:
        return n[0]+".00"
    if len(n)==2:
        f = n[1]
        if len(f)==1:
            f = f+"0"
            return n[0]+"."+f
        elif len(f)==2:
            return n[0]+"."+f
        else:
            f = f[:2]
            f = f[:1]+str(int(f[-1])+1)
            return n[0]+"."+f



        avg = str(sum(valids)/len(valids)*100)[:4]
        print(avg)
        print(avg[:-2], avg[-2:])


'''
from math import floor
def averageOfTopEmployees(rating):
    valids = [x for x in rating if x >= 90]
    if len(valids)>0:
        avg = sum(valids)/len(valids)
        avg += 0.001
        avg = round(avg, 2)
        print('{:04.2f}'.format(avg))      
    else:
        print("0.00")



if __name__ == '__main__':

    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)

