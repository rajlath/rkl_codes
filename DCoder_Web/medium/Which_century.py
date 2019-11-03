def get_ordinal_format(n):
    ordinals = ["st", "nd", "rd", "th"]
    n %= 100
    if 3 < n < 21 : return ordinals[3]
    mods = n % 10
    if mods == 1:return ordinals[0]
    elif mods == 2:return ordinals[1]
    elif mods == 3:return ordinals[2]
    else:return ordinals[3]

ins = int(input())
century = ins // 100 + 1
print(str(century) + get_ordinal_format(century))

