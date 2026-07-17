def count_codons(sequence):
    """
    Count codons in a DNA sequence.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        dict: Codon counts.
    """

    codons = {}

    for i in range(0, len(sequence) - 2, 3):

        codon = sequence[i:i + 3]

        if codon in codons:
            codons[codon] += 1
        else:
            codons[codon] = 1

    return codons