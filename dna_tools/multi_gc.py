from dna_tools.gc import calculate_gc_content


def gc_for_all_sequences(sequences):
    """
    Calculate GC content for all sequences.
    """

    results = {}

    for header, sequence in sequences.items():
        results[header] = calculate_gc_content(sequence)

    return results