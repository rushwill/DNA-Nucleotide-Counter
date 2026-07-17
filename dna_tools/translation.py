from dna_tools.codon_table import CODON_TABLE


def translate_dna(sequence):
    """
    Translate a DNA sequence into a protein sequence.
    """

    # DNA -> RNA
    rna = sequence.replace("T", "U")

    protein = ""

    for i in range(0, len(rna) - 2, 3):

        codon = rna[i:i+3]

        amino_acid = CODON_TABLE.get(codon)

        if amino_acid is None:
            protein += "?"

        elif amino_acid == "*":
            break

        else:
            protein += amino_acid

    return protein