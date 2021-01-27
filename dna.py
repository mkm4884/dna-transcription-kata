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
import re
import json



def antisense(input_DNA):
    flipped = input_DNA[::-1]
    anti = "".join([DNA_lookup[x] for x in flipped])
    return anti


def transcription(input_DNA):
    anti = antisense(input_DNA)
    anti = anti.replace("T","U")
    return anti


def findStart(input_RNA):
    start = "AUG"
    start_idxs = [m.start() for m in re.finditer(start, input_RNA)]
    # print(start_idxs)
    return start_idxs

input_DNA = "AGGACGGGCTAACTCCGCTCGTCACAAAGCGCAATGCAGCTATGGCAGATGTTCATGCCG"


DNA_lookup = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

with open("data/codons.json") as c:
    codon_lookup = json.load(c)

with open("data/peptides.json") as p:
    peptides_lookup = json.load(p)

antisense_DNA = antisense(input_DNA)
antisense_RNA = transcription(antisense_DNA)
sense_RNA = transcription(input_DNA)
antisense_starts = findStart(antisense_RNA)
sense_starts = findStart(sense_RNA)

for start in sense_starts:
    for idx in range(start, len(sense_RNA), 3):
        triplet = sense_RNA[idx:idx+3]
        print(triplet)
        codon = codon_lookup[triplet]
        print(codon)
        peptide = peptides_lookup[codon.lower()]
        print(peptide)












