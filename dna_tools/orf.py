def find_orf(sequence):
    """
    Find the first Open Reading Frame (ORF) in a DNA sequence.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        str | None: ORF sequence if found, otherwise None.
    """

    stop_codons = {"TAA", "TAG", "TGA"}

    for i in range(len(sequence) - 2):

        codon = sequence[i:i + 3]

        if codon == "ATG":

            for j in range(i, len(sequence) - 2, 3):

                current = sequence[j:j + 3]

                if current in stop_codons:
                    return sequence[i:j + 3]

    return None