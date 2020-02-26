
class Seq:
    def __init__(self, strbases):  # -- function for initializing the object "strbases": is a parameter , you can call whenever you want
        self.strbases = strbases

    def __str__(self):  # -- it will run each time something is print
        return self.strbases

    def len(self):  # -- self means inside the method
        return(len(self.strbases))

def print_seq(seq):
     # the function prints seqs(seq_list) that receives a list of sequence and prints their number in the list, their length and the sequence itself
    for s in seq:
        print(f"Sequence {seq.index(s)}: (Length: {s.len()}) {s}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seq(seq_list)