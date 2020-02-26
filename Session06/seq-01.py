class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):  # -- function for initializing the object "strbases": is a parameter , you can call whenever you want
        self.strbases = strbases    # -- internal variable inside de object when we use "self"
        print("New sequence created!")  # -- it is an special method that is called everytime a new object is created
    def __str__(self):  # -- it will run each time something is print
        return self.strbases  # -- it gives the internal info of the objects

    def len(self):  # -- self means inside the method
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

# -- As the Gene is also a Seq, for creating a Gene first we should call the init function from the Seq class.
# Then, do it by calling the super().init(strbases) method.
# Afterwards, we will add the properties of the Gene. In this case its' name.
# All the Genes are sequences