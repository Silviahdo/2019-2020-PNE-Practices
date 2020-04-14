from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

FOLDER = "../Session04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta(FOLDER + GENES[0] + EXT)

print(f"Sequence: (Length: {s.len()}) {s}")
print("  Bases:", s.count())
print("  Rev:", s.seq_reverse())
print("  Comp:", s.seq_complement())