'''
'''
def get_valid_cnt(x):
    t = 1
    while t*t < x:
        t<<=1
    if x//t >= t/2:return x - x//t
    else: return x - t//2 + 1

try:
    while True:
        start=True
        ins = input()
        if ins != '':
            if start==True:start=False
            else:
                print(get_valid_cnt(int(ins)))
        else:
            break
except EOFError:
    pass