from Seq0 import *

FOLDER = "../Session04/"
filename = ["U5.txt", "ADA.txt", "FRAT1.txt", "RNU6_269P.txt"]

list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for element in filename:
    seq = seq_read_fasta(FOLDER + element)
    print(seq_len(seq))

