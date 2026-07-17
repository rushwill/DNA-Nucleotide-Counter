from dna_tools.transcription import transcribe_dna


def test_transcription():
    assert transcribe_dna("ATCG") == "AUCG"


def test_only_thymine_changes():
    assert transcribe_dna("TTTT") == "UUUU"