def count_nucleotides(sequence):
    """
    Count the number of each nucleotide in a DNA sequence.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        dict: Counts of A, T, C, and G.
    """

    counts = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0,
    }

    for nucleotide in sequence:
        counts[nucleotide] += 1

    return counts