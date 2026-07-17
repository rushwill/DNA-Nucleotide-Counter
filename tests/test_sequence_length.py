from dna_tools.sequence_length import calculate_sequence_lengths


def test_sequence_lengths():

    sequences = {
        "seq1": "ATGC",
        "seq2": "AAAAAA",
    }

    result = calculate_sequence_lengths(sequences)

    assert result == {
        "seq1": 4,
        "seq2": 6,
    }