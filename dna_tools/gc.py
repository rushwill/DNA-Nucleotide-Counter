def calculate_gc_content(sequence):
    """
    Calculate GC content percentage.

    Parameters:
        sequence (str): Valid DNA sequence.

    Returns:
        float: GC percentage.
    """

    gc_count = 0
    
    if len(sequence) == 0:
        raise ValueError("DNA sequence cannot be empty.")

    for nucleotide in sequence:
        if nucleotide in ("G", "C"):
            gc_count += 1

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage