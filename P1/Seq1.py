from pathlib import Path  # for open a file


def valid_str(strbases):  # self argument is always the first
    valid_b = ["A", "C", "G", "T"]
    for b in strbases:
        if b not in valid_b:  # if there is any invalid base
            return False
    return True  # valid


class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):  # function for initializing the object #strsbases: is a parameter, you can
        # call wherever you want
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL sequence created")
            return

        if not valid_str(strbases):
            self.strbases = self.ERROR  # you have always have to put self to operate with an object
            print("INVALID Seq!")
            return

        # string in the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0  # a 0 if it is null or invalid
        else:
            return len(self.strbases)

    def seq_read_fasta(self, filename):
        #  read the text
        content = Path(filename).read_text()
        # Remove the head
        body = content.split('\n')[1:]

        # Store the sequence
        self.strbases = "".join(body)

        return self

    def seq_count_bases(self, b):  # it applies to the dictionary,
        return self.strbases.count(b)

    def count(self):  # times that a base is repited
        e = {"A": self.seq_count_bases("A"), 'T': self.seq_count_bases('T'),
             'C': self.seq_count_bases('C'), 'G': self.seq_count_bases('G')}

        return e

    def seq_reverse(self):
        if self.strbases in [self.NULL]:
            return "NULL"
        elif self.strbases in [self.ERROR]:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        e = {"A": "T", 'T': 'A', 'C': 'G', 'G': 'C'}
        es = ""
        if self.strbases in [self.NULL]:
            return "NULL"
        elif self.strbases in [self.ERROR]:
            return "ERROR"
        else:

            for b in self.strbases:
                es += e[b]

        return es

    def seq_count_base(self, param):
        pass
