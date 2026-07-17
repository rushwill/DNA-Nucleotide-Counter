def calculate_sequence_lengths(sequences):
    """
    Calculate the length of each DNA sequence.

    Parameters:
        sequences (dict): Dictionary of FASTA sequences.

    Returns:
        dict: Sequence lengths.
    """

    lengths = {}

    for header, sequence in sequences.items():
        lengths[header] = len(sequence)

    return lengths