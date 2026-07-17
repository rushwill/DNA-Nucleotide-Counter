def complement(sequence):
    """
    Generate the complementary DNA sequence.
    """

    complement_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    complement_sequence = ""

    for nucleotide in sequence:
        complement_sequence += complement_map[nucleotide]

    return complement_sequence