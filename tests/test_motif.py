from dna_tools.motif import find_motif


def test_find_motif():

    sequence = "GATATATGCATATACTT"

    motif = "ATAT"

    assert find_motif(sequence, motif) == [2, 4, 10]

def test_no_match():

    assert find_motif("AAAAAA", "CG") == []