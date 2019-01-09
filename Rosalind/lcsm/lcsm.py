import os
#open input file
inpath = os.path.dirname(os.path.abspath(__file__))
filename= "rosalind_lcsm.txt"
ifile = open(inpath + "\\" + filename)

text = [line.strip() for line in ifile]
i = 2
while i < len(text):
    if not text[i].startswith('>') and not text[i-1].startswith('>'):
        text[i-1] += text[i]
        del text[i]
        i -= 1
    i += 1
i = 0
while i < len(text):
    del text[i]
    i += 1

def LCS( text ):
    valid = []
    for k in range(len(text[0]),1,-1):
        for start in range(len(text[0])-k+1):
            curr = text[0][start:start+k]
            found = True
            for i in range(1,len(text)):
                if not curr in text[i]:
                    found = False
                    break
            if found:
                valid.append(curr)
    return valid
valid = LCS(text)
print(max(valid))



