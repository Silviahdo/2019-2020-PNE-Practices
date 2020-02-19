from Seq0 import *

FOLDER = "../Session04/"
filename = ".txt"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'C', 'T', 'G']

GENE = list_genes[0]
print(f"Gene {GENE}:")
seq = seq_read_fasta(FOLDER + list_genes[0] + filename)[:20]
rev = seq_reverse(seq)
print(f"Frag: {seq}")
print(f"Rev : {rev}")