import http.client
import json
import termcolor as tc
from Seq1 import Seq


def sequence_information(bases):
    seq_info = Seq(bases)
    min_count = 0
    most_frecuent_base = ""

    tc.cprint("Total length:", 'green', end=' ')
    print(seq_info.len())

    for base, count in seq_info.count().items():
        # -- Returns the base and count from each .item()
        percentage = round(count / seq_info.len() * 100, 2)
        tc.cprint(f"{base}:", 'blue', end=' ')
        print(f" {count} ({percentage}%)")

        # -- Most frequent bases
        if min_count < count:
            min_count = count
            most_frecuent_base = base

    tc.cprint("Most frequent Base:", 'green', end=' ')
    print(most_frecuent_base)


GENES = dict(FRAT1='ENSG00000165879',  # defining the dictionary
             ADA='ENSG00000196839',
             FXN='ENSG00000165060',
             RNU6_269P='ENSG00000212379',
             MIR633='ENSG00000207552',
             TTTY4C='ENSG00000228296',
             RBMY2YP='ENSG00000227633',
             FGFR3='ENSG00000068078',
             KDR='ENSG00000128052',
             ANK2='ENSG00000145362')

gene = input('Write the gene name:')

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
OPTIONS = GENES[gene] + '?content-type=application/json'
METHOD = "GET"
URL = SERVER + ENDPOINT + OPTIONS

print(f"\nConnecting to server: {SERVER}")
print(f"URL : {URL}")

# Connect w the server
connect = http.client.HTTPConnection(SERVER)

try:
    connect.request(METHOD, ENDPOINT + OPTIONS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# response and status
response = connect.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")

data = response.read().decode("utf-8")
# -- Read JSON
info_api = json.loads(data)

# -- INFO
sequence = (info_api['seq'])
description = info_api['desc']

# -- RESULTS
tc.cprint("Gene: ", 'green', end="")
print(gene)

tc.cprint("Description: ", 'green', end="")
print(description)

sequence_information(sequence)
