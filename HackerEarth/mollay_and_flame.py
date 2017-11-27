'''
SAMPLE INPUT
2
sherlock molly
watson mary
SAMPLE OUTPUT
2
FALME
FALME

10
azttckdrsrvyptxpwjxzfdedlgcsy otqalyijmbqhbwuqkhbwuimqbrpqcj
vqlecjjjmtofddylowrujavptiodu piuxncddiyugnukknzqofdkefsjbkz
qyvyzrvhfjxxjqelhgwvjkuuyanwqo ekradixfsjktjwomemclsmlbpamsa
sexvxbwuysvafgpbogixtgkvfxfjnf drxzegojnlvfbkhiaatarmrshewkd
vxzcjzqhetmiiqredqtfwximhejkj rijclkrluyxqvgxjbyzkofmitsssh
oxihaqepjtbolkjmcszwmbkzjzrxk mdfunqniverdcrxaojlllohmriumkd
ocsjchjdkzedlrzcrxfgosfvqoyncz kjosrvuockfmgylunzafuxhcvnopc
znvyeefutbrtawsdslmukkzijjooik rygdhouvvuabhnrkyoydhfidgtuml
pgazdfgsvzdgsfradpbjikdhykjnm unsqbsebhekhalnpijhgatwdxhhjt
vnpdzgxmtatsnofmggvqnvktgqvtka fyiupsmelixmptfdizdscjhdgybgro

LFAME
FALME
FMALE
FALME
LFAME
FALME
FEAML
FMALE
FLAME
LFAME
'''
for _ in range(int(input())):
    a, b = input().split()
    x_rem = len(set(a) - set(b)) + len(set(b) - set(a))
    l_at = 1
    l_be = (x_rem % 5)-1

    s = list("FLAME")
    s[l_at], s[l_be] = s[l_be], s[l_at]
    print("".join(s))