def find_motif(sequence, motif):
    """
    Find all positions of a motif in a DNA sequence.

    Parameters:
        sequence (str): DNA sequence.
        motif (str): DNA motif.

    Returns:
        list: 1-based positions where the motif occurs.
    """

    positions = []

    sequence = sequence.upper()
    motif = motif.upper()

    motif_length = len(motif)

    for i in range(len(sequence) - motif_length + 1):

        if sequence[i:i + motif_length] == motif:
            positions.append(i + 1)

    return positions