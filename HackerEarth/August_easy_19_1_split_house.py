lens = int(input())
has  = ["H" if x == "H" else "B" for x in input()]
has  = "".join(has)
if "HH" in has:
    print("NO")
else:
    print("YES")
    print(has)