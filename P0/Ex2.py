from Seq0 import *

FOLDER = "../Session04/"
filename = "U5.txt"

print("DNA file:", filename)
seq = seq_read_fasta(FOLDER + filename)
print("The first 20 bases are:", seq[0:20])

