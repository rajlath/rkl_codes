CODON_MAP = (
    (('AUG',),'Methionine'),
    (('UUU', 'UUC'),'Phenylalanine'),
    (('UUA', 'UUG'),'Leucine'),
    (('UCU', 'UCC', 'UCA', 'UCG'),'Serine'),
    (('UAU', 'UAC'),'Tyrosine'),
    (('UGU', 'UGC'),'Cysteine'),
    (('UGG',),'Tryptophan'),
    (('UAA', 'UAG', 'UGA'),'STOP'))

PROTEINS = { codon: name for codons, name in CODON_MAP for codon in codons }

def proteins(strand):
    rets = []
    for i in range(0, len(strand), 3):
        curr = strand[i:i+3]
        protein = PROTEINS[curr]
        if protein == 'STOP' or len(curr) < 3:
            return rets
        if protein is not None:rets.append(protein)
    return rets


proteins("UGGUGUUAUUAAUGGUUU")
