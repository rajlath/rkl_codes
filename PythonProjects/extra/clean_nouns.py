res_file = open("noun.txt", "w")
with open("nouns.txt") as f:
    for line in f:
        curr = line.split()[0]
        if len(curr) in [4, 5]:
            print(line.split()[0], file=res_file)
print("done")        
        