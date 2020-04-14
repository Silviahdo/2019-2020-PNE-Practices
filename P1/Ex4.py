from Seq1 import Seq

print("-----| Practice 1, Exercise 4 |------")
# -- Create a Null sequence
seq1 = Seq()

# -- Create a valid sequence
seq2 = Seq("ACTGA")

# -- Create an invalid sequence
seq3 = Seq("Invalid sequence")

print(f"Sequence1: (Length: {seq1.len()}) {seq1}")
print(f"Sequence2: (Length: {seq2.len()}) {seq2}")
print(f"Sequence3: (Length: {seq3.len()}) {seq3}")