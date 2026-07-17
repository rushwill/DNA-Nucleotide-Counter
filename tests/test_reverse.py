from dna_tools.reverse import reverse_sequence


def test_reverse():
    assert reverse_sequence("TAGC") == "CGAT"


def test_single_nucleotide():
    assert reverse_sequence("A") == "A"


def test_empty_sequence():
    assert reverse_sequence("") == ""