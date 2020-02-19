from Seq0 import *

FOLDER = "../Session04/"
BASES = ["A", "C", "T", "G"]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for element in list_genes:
    sequence = seq_read_fasta(FOLDER + element + ".txt")
    dict_bases = seq_count(sequence)
    min_value = 0
    best_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            best_base = base

    print("Gene", element, ": Most frequent base: ", best_base)