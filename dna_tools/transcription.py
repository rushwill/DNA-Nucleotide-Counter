def transcribe_dna(sequence):
    """
    Convert a DNA sequence to an RNA sequence.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        str: RNA sequence.
    """

    return sequence.replace("T", "U")