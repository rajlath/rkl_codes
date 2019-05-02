def solve(ch, less):
    ans = [None] * len(ch)
    ls  = 0
    for i in range(len(ch)):
        if ls > 0:ans[i] = '0'
        elif ls < 0: ans[i] = '8'
        else:
            if int(ch[i]) % 2 == 0:ans[i] = ch[i]
            else:
                if less:
                    ans[i] = chr(ord(ch[i]) - 1)
                    ls = -1
                else:
                    if ch[i] == '9': return None
                    ans[i] = chr(ord(ch[i]) + 1)
                    ls = 1
    return ans
insi = input()
insii= int(insi)
ans = int(10 ** 18)
ins = [x for x in insi]
a = solve(ins, False)
if a is not None:
    ai = abs(insii - int(''.join(a)))
    ans = min(ai, ans)
b = solve(ins, True)
if b is not None:
    bi = abs(insii - int(''.join(b)))
    ans = min(bi, ans)

print(ans)