from dna_tools.complement import complement


def test_complement():
    assert complement("ATCG") == "TAGC"


def test_single_nucleotide():
    assert complement("A") == "T"


def test_empty_sequence():
    assert complement("") == ""