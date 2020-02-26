class Seq:
    def __init__(self, strbases):  # function for initializing the object "strbases": is a parameter , you can call whenever you want
        self.strbases = strbases   # passed as argument when creating the object
        print("New sequence created!") # it is an special method that is called everytime a new object is created

        bases = ['A', 'C', 'G', 'T']

        for base in strbases:
            if base not in bases:
                print("ERROR!!")
                print("Sequence 2: ERROR!")
            return

        self.strbases

    def __str__(self): # -- It run each time something is print
        return self.strbases # It gives the internal info os the object

    def len(self):
        return(self.strbases)

s1 = Seq("AACGTC") # viene de la clase
s2 = Seq("Hello? Am I valid sequence?")
print(f"Sequence 2: {s1} ")