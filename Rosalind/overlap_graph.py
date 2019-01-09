import sys
k = 3

text = [line.strip() for line in open('E:\\rkl_codes\\Rosalind\\rosalind_grph.txt')]
i = 2
while i < len(text):
    if not text[i].startswith(">") and not text[i-1].startswith(">"):
        text[i-1] += text[i]
        del text[i]
        i -= 1
    i += 1
dna = {}
for i in range(0, len(text), 2):
    dna[text[i][1:]] = text[i-1]
for first in dna.keys():
    for second in dna.keys():
        if first != second and dna[]

