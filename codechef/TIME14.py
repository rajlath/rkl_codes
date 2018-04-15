
ins = "AELMORSU"
out =["?!", "?", "?!??", "!!", "!!!", "?!?", "???", "??!"]

print("".join([out[ins.index(x)] for x in input()]))