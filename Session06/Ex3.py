class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):  # -- function for initializing the object "strbases": is a parameter , you can call whenever you want
        self.strbases = strbases    # -- internal variable inside de object when we use "self"
        print("New sequence created!")  # -- it is an special method that is called everytime a new object is created
    def __str__(self):  # -- it will run each time something is print
        return self.strbases  # -- it gives the internal info of the objects

    def len(self):  # -- self means inside the method
        return(len(self.strbases))


def print_seq(seq):
    # the function prints seqs(seq_list) that receives a list of sequence and prints their number in the list, their length and the sequence itself
    for s in seq:
        print(f"Sequence {seq.index(s)}: (Length: {s.len()}) {s}")

def generate_seq(seq, number):
    seqs=[]
    for letter in range(1, number + 1):
        seqs.append(Seq(seq*letter))
    return seqs

seq_list1 = generate_seq("A", 3)
seq_list2 = generate_seq("AC", 5)

print("List 1:")
print_seq(seq_list1)

print()
print("List 2:")
print_seq(seq_list2)