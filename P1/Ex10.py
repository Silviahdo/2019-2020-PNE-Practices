from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

FOLDER = "../Session04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ['A', 'C', 'T', 'G']

for g in GENES:
    se = Seq().seq_read_fasta(FOLDER + g + EXT)
    dictionary = se.count()
    lit = list(dictionary.values())
    most_common = max(lit)
    print("Gene ", g, ": Most frequent Base:", bases[lit.index(most_common)])