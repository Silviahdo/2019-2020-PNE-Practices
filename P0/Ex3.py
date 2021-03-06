from Seq0 import *

FOLDER = "../Session04/"
filename = ".txt"

list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for element in list_genes:
    seq = seq_read_fasta(FOLDER + element + filename)
    print(f"Gene {element} length is {seq_len(seq)}")

