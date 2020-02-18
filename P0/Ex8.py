from Seq0 import*

PRACTICE = 8
FOLDER = "../Session04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ["A", "C", "T", "G"]

print(f"-----|Exercice {PRACTICE}|-----")

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)

    # --Dictionary with the values
    d = seq_count(seq)

    # --Create a list with all the values
    ll = list(d.values())

    # -- Calculates the maximum
    m = max(ll)
#practice 8 as professor did