class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases    # -- internal variable inside de object when we use "self"
        print("New sequence created!")
    def __str__(self):
        return self.strbases

    def len(self):
        return(len(self.strbases))
    pass    # -- There is nothing inside this class

class Gene(Seq):
    pass

# --Main program
s1 = Seq("AACGTC")
g = Gene("ACCTGA")
s2 = Seq("CCGTCGA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Gene sequence: {g}")
l1 = s1.len()
print(f"The length of the sequence 1 is {l1}")
print(f"The length of the sequence 2 is {s2.len()}")
print(f"The length of the genes is {g.len()}")

print("Testing objects...")

