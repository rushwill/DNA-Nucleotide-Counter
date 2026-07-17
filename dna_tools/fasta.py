def read_fasta(file_path):
    """
    Read sequences from a FASTA file.

    Returns:
        dict
    """

    sequences = {}

    current_header = None
    current_sequence = []

    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                if current_header is not None:
                    sequences[current_header] = "".join(current_sequence)

                current_header = line[1:]
                current_sequence = []

            else:
                current_sequence.append(line.upper())

        if current_header is not None:
            sequences[current_header] = "".join(current_sequence)

    return sequences