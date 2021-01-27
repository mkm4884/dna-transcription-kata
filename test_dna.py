import dna
import pytest

@pytest.fixture()
def test():
    return "ACGTT"


def test_antisense(test):
    assert dna.antisense(test) == "AACGT"


def test_transcription(test):
    assert dna.transcription(test) == "AACGU"


def test_findStart():
    assert dna.findStart("CAUGUACCAUG") == [1, 8]