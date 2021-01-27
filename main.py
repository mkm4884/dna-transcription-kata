'''
Input: str - DNA sequence
Load JSONs
Create lookup dictionary to make the antisense strand
Make antisense strand
flip antisense strand
Convert to RNA (both strands)
Loop through the strands, read codons, save index of AUG
- if start codon:
    loop through in increments of 3
    lookup AA, lookup single letter AA, and append single letter AA
    find first stop codon - store in list, break loop
Output Protein seq
'''
import pytest

input_DNA = "AGGACGGGCTAACTCCGCTCGTCACAAAGCGCAATGCAGCTATGGCAGATGTTCATGCCG"


DNA_lookup = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

def antisense(input_DNA):
    flipped = input_DNA[::-1]
    anti = "".join([DNA_lookup[x] for x in flipped])
    return anti

def transcription(input_DNA):
    pass


test = "ACGTT"

def test_antisense():
    assert antisense(test) == "AACGT"

def test_transcription():
    assert transcription(test) == "AACGU"





