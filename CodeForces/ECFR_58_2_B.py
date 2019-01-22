ins = input()
opn_brk = ins.find("[")
opn_cln = ins.find(":", opn_brk)
clo_brk = ins.rfind("]")
clo_cln = ins.rfind(":", opn_cln , clo_brk)
if opn_brk < opn_cln < clo_cln < clo_brk and opn_brk != -1 and opn_cln != -1 and clo_cln != -1:
    bar_cnt = ins[opn_cln+1:clo_cln].count("|")
    print(bar_cnt + 4)
else:
    print(-1)










