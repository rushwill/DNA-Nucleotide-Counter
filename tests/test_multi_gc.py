from dna_tools.multi_gc import gc_for_all_sequences


def test_gc():

    sequences = {
        "seq1": "ATGC",
        "seq2": "AAAA"
    }

    result = gc_for_all_sequences(sequences)

    assert result["seq1"] == 50.0
    assert result["seq2"] == 0.0