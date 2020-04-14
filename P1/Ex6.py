from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
# -- Create a Null sequence
seq1 = Seq()

# -- Create a valid sequence
seq2 = Seq("ACTGA")

# -- Create an invalid sequence
seq3 = Seq("Invalid sequence")

for i, e in enumerate([seq1, seq2, seq3]):
    print(f"Sequence{i}: (Length: {e.len()}) {e}")
    print("  Bases:", e.count())