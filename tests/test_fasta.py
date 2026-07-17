from dna_tools.fasta import read_fasta


def test_read_fasta():

    sequences = read_fasta("sample.fasta")

    assert "Sequence1" in sequences
    assert sequences["Sequence1"] == "ATCGATCGATCG"