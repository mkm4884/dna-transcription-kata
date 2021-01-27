import dna

test = "ACGTT"
test2 = "CAUGUACCAUG"

def test_antisense():
    assert dna.antisense(test) == "AACGT"

def test_transcription():
    assert dna.transcription(test) == "AACGU"

def test_findStart():
    assert dna.findStart(test2) == [1, 8]