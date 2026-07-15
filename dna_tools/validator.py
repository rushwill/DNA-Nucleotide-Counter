def validate_dna(sequence):
    """
    Validate a DNA sequence.

    Parameters:
        sequence (str): DNA sequence entered by the user.

    Returns:
        str: Uppercase validated DNA sequence.

    Raises:
        ValueError: If the sequence contains invalid characters.
    """

    sequence = sequence.upper()

    valid_nucleotides = {"A", "T", "C", "G"}

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(
                f"Invalid nucleotide '{nucleotide}'. Only A, T, C, and G are allowed."
            )

    return sequence