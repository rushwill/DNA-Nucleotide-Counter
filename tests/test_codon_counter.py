from dna_tools.codon_counter import count_codons


def test_count_codons():

    result = count_codons("ATGAAATTTATG")

    assert result == {
        "ATG": 2,
        "AAA": 1,
        "TTT": 1,
    }

def test_empty_sequence():

    assert count_codons("") == {}