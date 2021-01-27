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

def seq(input_DNA):
