
from collections import Counter
for i in range(int(input())):
    front = input()
    backs = input()
    fc    = Counter(front)
    bc    = Counter(backs)
    if "b" in fc:
        if fc["b"] == 2:
            if "o" in fc:
                ans = "yes"
            else:
                ans = "no"
                if "o" in bc:
                    for i, v in enumerate(bc["o"]):
                        if i not in fc["b"]:
                            ans = "yes"
                            break
        if ans == "no":
            if fc["b"] == 1:









