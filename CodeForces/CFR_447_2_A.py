ins = input()
q_cnt = ins.count("Q")
qs, has = 0, 0
for i, ch in enumerate(ins):
    if ch == "A":
        has += qs * (q_cnt - qs)
    elif ch == 'Q':
        qs += 1
print(has)