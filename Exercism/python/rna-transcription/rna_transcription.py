
import string
def to_rna(dna_strand):
    intab = "GCTA"
    outtab = "CGAU"
    trantab = str.maketrans(intab, outtab)
    return dna_strand.translate(trantab)


