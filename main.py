import json

from dna import antisense, transcription, findStart


def main():
    input_DNA = "AGGACGGGCTAACTCCGCTCGTCACAAAGCGCAATGCAGCTATGGCAGATGTTCATGCCG"



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
            triplet = sense_RNA[idx:idx + 3]
            print(triplet)
            codon = codon_lookup[triplet]
            print(codon)
            peptide = peptides_lookup[codon.lower()]
            print(peptide)


if __name__ == '__main__':
    main()
