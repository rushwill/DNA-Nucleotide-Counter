from dna_tools.orf import find_orf


def test_find_orf():
    assert find_orf("AAAATGCCCGGGTAA") == "ATGCCCGGGTAA"


def test_no_orf():
    assert find_orf("AAACCCGGG") is None