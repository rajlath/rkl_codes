necklace = input()
perl_count = necklace.count("o")
link_count = len(necklace) - perl_count
if perl_count == 0 or link_count % perl_count == 0:
    print("YES")
else:
    print("NO")


