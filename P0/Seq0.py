from pathlib import Path

def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
   file_contents = Path(filename).read_text()
   file = file_contents.split('\n')
   body = "".join(file[1:])
   return(body)

def seq_len(seq):
    return(len(seq))





