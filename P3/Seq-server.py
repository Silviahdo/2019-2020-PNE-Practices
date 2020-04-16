from Seq1 import Seq
import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"

# -- Invented sequence for the GET command
get_seq = [
    "AACTGATTTGCTAATCGTCTGATAGCTTTCGGAATCCTGATGCTTATGGCT",
    "CGTAGCTGAACGGTCGTAAGCTTAGATTAAGCTAGAAGTCAAAAGGCTATC",
    "TGATCCTAAAGTAGGCTTAAGCCCTGATCGGGATTTCGCCCGAATGCTAGC",
    "AGTCTCGATCGCTCAGATCGATCGTAGCTAATCGCTGGCTAGCTAGCTGAT",
    "GCACGGTTTTCGTACGATATAGGCTAGCTAGCTTAGCTAGCTAGCGTAGCG",
]

FOLDER = "../Session04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

# -- Returns a sequence of the position given by the user
def get_command(n):
    return get_seq[n]

# -- Returns the string given with the information
def info_command(sequence):
    # -- Creates the object sequence from the string
    s = Seq(sequence)
    # -- Measure the length of the object to count bases and calculate its percentage(%)
    str_length = s.len()
    count_A = s.seq_count_bases('A')
    pa = "{:.1f}".format(100 * count_A / str_length)
    count_C = s.seq_count_bases('C')
    pc = "{:.1f}".format(100 * count_C / str_length)
    count_T = s.seq_count_bases('T')
    pt = "{:.1f}".format(100 * count_T / str_length)
    count_G = s.seq_count_bases('G')
    pg = "{:.1f}".format(100 * count_G / str_length)

    result = f"""Sequence: {s}
Total length: {str_length}
A: {count_A} ({pa}%)
C: {count_C} ({pc}%)
T: {count_T} ({pt}%)
G: {count_G} ({pg}%)"""
    return result

# -- Returns a response with the complement of the sequence (ex: COMP ACTGTCTG)
def comp_command(sequence):
    # -- First we create the object seq from the string and then we use a function from the class Seq
    s = Seq(sequence)
    return s.seq_complement()

# -- Returns a response with the reverse of the given sequence
def rev_command(sequence):
    # -- First we create the object seq from the string and then we use a function from the class Seq
    s = Seq(sequence)
    return s.seq_reverse()

# -- Returns the complete sequence of the gene
def gene_command(name):
    s = Seq()
    s.seq_read_fasta(FOLDER + name + EXT)
    return str(s)

# Configure the server
listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listening_socket.bind((IP, PORT))

listening_socket.listen()

print("SEQ Server configured!")

# -- Main loop program
while True:
    print("Waiting for clients....")
    try:
        (client_socket, client_ip_port) = listening_socket.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        listening_socket.close()
        exit()
    else:
        req_raw = client_socket.recv(2000)
        req = req_raw.decode()

        # Process the command
        lines = req.split("\n")
        line0 = lines[0].strip()

        # Separate the line into command an argument
        line_comands = line0.split(' ')

        # First element is the command
        command = line_comands[0]

        # Get the first argument
        try:
            argument = line_comands[1]
        except IndexError:
            argument = ""

        response = ""

        if command == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif command == "GET":
            termcolor.cprint("GET", 'green')
            response = get_command(int(argument))
        elif command == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_command(argument)
        elif command == "COMP":
            termcolor.cprint("COMP", 'green')
            response = comp_command(argument)
        elif command == "REV":
            termcolor.cprint("REV", 'green')
            response = rev_command(argument)
        elif command == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_command(argument)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        response += '\n'
        print(response)
        client_socket.send(response.encode())
        client_socket.close()



