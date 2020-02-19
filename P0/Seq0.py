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

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    res = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'), 'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return res

def seq_perc(seq):
    num = seq_count(seq)
    for b in ['A', 'T', 'C', 'G']:
        num[b] = round(100.0 * num[b] / seq_len(seq), 1)
    return num


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(seq):
    basec = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    res = ""

    for b in seq:
        res += basec[b]

    return res