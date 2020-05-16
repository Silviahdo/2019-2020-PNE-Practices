from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session04/"
GENE = "FRAT1"
FILENAME = "FRAT1.txt"
DNA_FILE = FOLDER + FILENAME

# -- Create 2 client objects for each server
c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)

print(c1)
print(c2)

# -- Read the Gene from a file
s = Seq().read_fasta(DNA_FILE)

# -- Get the gene string
bases = str(s)

# -- Print the Gene on the console
print(f"Gene {GENE}: {bases}")

LENGTH = 10

# -- Heading message for both servers
heading = f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases..."

c1.talk(heading)
c2.talk(heading)

for i in range(10):

    fragment = bases[i*LENGTH:(i+1)*LENGTH]

    # -- Print on Client's console
    print(f"Fragment {i+1}: {fragment}")

    sms = (f"Fragment {i+1}: {fragment}")

    # -- even fragments (counting from 0) are sent to server 1
    if i % 2:
        c2.talk(sms)

    # -- Odd segments are sent to server 2
    else:
        c1.talk(sms)