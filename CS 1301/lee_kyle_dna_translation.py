"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

"""

import lee_kyle_helper

def transcription(dna_sequence):
    Base_pair_table = {
        "A" : "U",
        "U" : "A",
        "C" : "G",
        "G" : "C"
    }
    mrna_sequence = dna_sequence.replace("T","U")

    complement = ''
    for i in range(0,len(mrna_sequence)):
        complement += Base_pair_table[mrna_sequence[i]]

    return complement

def translate(mrna):
    protein = ''

    chunky = lee_kyle_helper.chunk(mrna,3)
    for i in chunky:
        protein += lee_kyle_helper.amino_acids[i] + ' '

    return protein


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

print(f"DNA Sequence\n{dna}\n")
print(f"MRNA Sequence\n{transcription(dna)}\n")
print(f"Protein Sequence\n{translate(transcription(dna))}\n")
