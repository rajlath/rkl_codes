print("\n".join([str(x) for x in range(0,51) if bin(x)[2:].count("1")&1==0]))

print(bin(45)[2:])