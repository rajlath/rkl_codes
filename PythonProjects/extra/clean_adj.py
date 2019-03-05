import re
res_file = open("adjective.txt", "w")
with open("adjectives.txt") as f:
    for line in f:
        re.sub(r"<li class=\"[a-z]\">", "", line)
        re.sub(r"</li>", "", line)
        words = line.split()
        for word in words:
            if len(word) in [4, 5]:
                print(word, file = res_file)
print("done")                