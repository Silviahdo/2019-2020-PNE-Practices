import http.server
import socketserver
from Seq1 import Seq

import requests

PORT = 8080

SERVER = 'http://rest.ensembl.org'
ENDPOINTS = ["/listSpecies", "/karyotype", "/chromosomeLength", "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]
ext = ['/info/species?', '/info/assembly/', "/xrefs/symbol/homo_sapiens/", '/sequence/id/', "/overlap/region/human/"]
CONTENT_TYPE = "?content-type=application/json"

# Prevents Error
socketserver.TCPServer.allow_reuse_address = True

#  Class with our handler that derived from the BaseHTTPRequestHandler and inherits all its properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        request_line = self.requestline
        command = self.command
        path = self.path
        contents = ""

        print("Request line:", request_line)
        print("  Command: ", command)
        print("  Path: ", path)

        if path == "/" or path == "/index.html":
            # The main page will be shown
            with open("index.html", 'r') as f:
                contents = f.read()

        elif path != "/" and path != "index.html":
            option = path.split('?')

# BASIC LEVEL
# ---> listSpecies endpoint

            if option[0] == ENDPOINTS[0]:
                connect = requests.get(SERVER + ext[0], headers={"Content-Type": "application/json"})
                data = connect.json()

                try:
                    li = option[1]
                    limit = li.split("=")[1]
                except IndexError:
                    limit = 0

                if limit != "":
                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Species List</title>
                                   </head>
                                   <body style="background-color: lightcyan;">
                                   <h1><b><FONT face = "Courier New">List of species</b></FONT></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p>The total number of species in the ensembl is: 286 <p>
                                   <p>You have selected the limit: {} <p>
                                   <p>The names of the species are: <P>
                                   <ol> {} </ol>
                                   </body>
                                   </html>"""

                    species_list = ""
                    # this is a loop that stops at the limit
                    for i in range(len(data['species'][:int(limit)])):
                        species_list = species_list + "<li>"
                        species_list = species_list + data['species'][i]['common_name']
                        species_list = species_list + "</li>"
                    species_list = species_list + "</ol></body></html>"
                    contents = contents.format(limit, species_list)

                elif limit == "":
                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Species List</title>
                                   </head>
                                   <body style="background-color: lightcyan;">
                                   <h1><b><FONT face = "Courier New">List of species</b></FONT></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p>The total number of species in the ensembl is: 286 <p>
                                   <p>You have not selected a limit <p>
                                   <p>The names of the species are: <P>
                                   <ol> {} </ol>
                                   </body>
                                   </html>"""

                    species_list = ""
                    for i in range(len(data['species'])):
                        species_list = species_list + "<li>"
                        species_list = species_list + data['species'][i]['common_name']
                        species_list = species_list + "</li>"
                    species_list = species_list + "</ol></body></html>"
                    contents = contents.format(species_list)

# ---> Karyotype endpoint

            elif option[0] == ENDPOINTS[1]:
                try:
                    sp = option[1].split("=")
                    specie = sp[1]

                    print("The specie to study is: ", specie)

                    connect = requests.get(SERVER + ext[1] + specie, headers={"Content-Type": "application/json"})
                    data = connect.json()

                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Karyotype</title>
                                   </head>
                                   <body style="background-color: lightcyan;">
                                   <h1><b><FONT face = "Courier New">Karyotype</b></FONT></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p> Names of the chromosomes of the: {} <P>
                                   <ol> {} </ol>

                                   </body>
                                   </html>"""
                    karyo_list = list(data['karyotype'])
                    if karyo_list != list():
                        k_list = ""
                        for crom in karyo_list:
                            if crom == "MT":
                                pass
                            elif crom != "MT":
                                k_list = k_list + "<li type=square>"
                                k_list = k_list + crom
                                k_list = k_list + "</li>"
                        contents = contents.format(specie, k_list)
                    elif karyo_list == list():
                        k_list = "Sorry, we don't have information about the karyotype of this specie"

                        contents = contents.format(specie, k_list)

                except KeyError:
                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Error</title>
                                       </head>
                                       <body style="background-color: #FE2E2E;">
                                       <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                       <a href="/"> Main page </a>
                                       <hr>
                                       <p> Sorry this specie is not valid </p>
                                       </body>
                                       </html>"""

# ---> Chromosome Length endpoint

            elif option[0] == ENDPOINTS[2]:
                try:
                    sp = option[1]
                    spe = sp.split("&")[0]
                    c = sp.split("&")[1]
                    specie = spe.split("=")[1]
                    chromo = c.split("=")[1]
                    conn = requests.get(SERVER + ext[1] + specie, headers={"Content-Type": "application/json"})
                    data = conn.json()

                    length = None
                    try:

                        for i in data['top_level_region']:
                            if i['coord_system'] == 'chromosome' and i['name'] == chromo:
                                length = i['length']

                        if length != None:
                            contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Length</title>
                                           </head>
                                           <body style="background-color: lightcyan;">
                                           <h1><b><FONT face = "Courier New">Chromosome length</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Selected specie: {}</p>
                                           <p> Selected chromosome: {}</p>
                                           <p> Length of the chromosome: {} <P>
                                           </body>
                                           </html>"""
                            contents = contents.format(specie, chromo, length)
                        else:
                            contents = """<!DOCTYPE html> 
                                               <html lang="en"> 
                                               <head>
                                                    <meta charset="UTF-8">
                                                    <title>Error</title>
                                               </head>
                                               <body style="background-color: #FE2E2E;">
                                               <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                               <a href="/"> Main page </a>
                                               <hr>
                                               <p> Sorry, this chromosome is not valid for the specie you choose</p>
                                               </body>
                                               </html>"""

                    except IndexError:
                        contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please enter a valid specie and chromosome </p>
                                           </body>
                                           </html>"""

                except KeyError:
                    contents = """<!DOCTYPE html> 
                                               <html lang="en"> 
                                               <head>
                                                    <meta charset="UTF-8">
                                                    <title>Error</title>
                                               </head>
                                               <body style="background-color: #FE2E2E;">
                                               <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                               <a href="/"> Main page </a>
                                               <hr>
                                               <p> Please enter a valid specie and chromosome </p>
                                               </body>
                                               </html>"""

# MEDIUM LEVEL
# ---> Gene sequence

            elif option[0] == ENDPOINTS[3]:
                self.send_response(200)
                gene = option[1].split("=")[1]
                try:
                    connect1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = connect1.json()
                    i = data1[0]
                    id = i["id"]
                    connect2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = connect2.json()
                    seq = data2["seq"]

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: lightcyan;">
                                       <h1><b><FONT face = "Courier New">Gene sequence</b></FONT></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p> Sequence: </p>
                                       <textarea readonly rows="60" cols="75" style="background-color:#F6D8FF"> {} </textarea>

                                       </body>
                                       </html>"""

                    contents = contents.format(gene, seq)
                except IndexError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""

                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""

            elif option[0] == ENDPOINTS[4]:
                self.send_response(200)
                gene = option[1].split("=")[1]
                try:
                    connect1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = connect1.json()
                    i = data1[0]
                    id = i["id"]
                    connect2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = connect2.json()
                    seq = data2["seq"]
                    c = data2["desc"]
                    h = c.split("chromosome:")
                    n = h[1].split(":")
                    start = n[2]
                    end = n[3]
                    ch = n[1]
                    length = len(seq)
                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Info</title>
                                       </head>
                                       <body style="background-color: lightcyan;">
                                       <h1><b><FONT face = "Courier New">Information about the gene </b></FONT></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p><b>Information: </b></p>
                                       <P> Id: {} </p>
                                       <p> Length: {}</p>
                                       <p> End: {}</p>
                                       <p> Start: {}</p>
                                       <p> Chromosome: {}</p>
                                       </body>
                                       </html>"""
                    contents = contents.format(gene, id, length, end, start, ch)
                except IndexError:
                    contents = """<!DOCTYPE html> 
                          <html lang="en"> 
                          <head>
                               <meta charset="UTF-8">
                               <title>Error</title>
                          </head>
                          <body style="background-color: #FE2E2E;">
                          <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                          <a href="/"> Main page </a>
                          <hr>
                          <p> Please write a valid human gene </p>
                          </body>
                          </html>"""
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""

            elif option[0] == ENDPOINTS[5]:
                self.send_response(200)
                gene = option[1].split("=")[1]
                try:
                    connect1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = connect1.json()
                    i = data1[0]
                    id = i["id"]
                    connect2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = connect2.json()
                    sequence = data2["seq"]
                    seq = Seq(sequence)

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: lightcyan;">
                                       <h1><b><FONT face = "Courier New">Calculations</b></FONT></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p> The length of the sequence is: {} </P>
                                       <p>The percentage of A is: {} %</p>
                                       <p>The percentage of G is: {} %</p>
                                       <p>The percentage of C is: {} %</p>
                                       <p>The percentage of T is: {} %</p>



                                       </body>
                                       </html>"""
                    portA = round(seq.seq_count_bases("A") / len(sequence), 2)
                    portG = round(seq.seq_count_bases("G") / len(sequence), 2)
                    portC = round(seq.seq_count_bases("C") / len(sequence), 2)
                    portT = round(seq.seq_count_bases("T") / len(sequence), 2)

                    contents = contents.format(gene, len(sequence), portA, portG, portC, portT)

                except IndexError:
                    contents = """<!DOCTYPE html> 
                          <html lang="en"> 
                          <head>
                               <meta charset="UTF-8">
                               <title>Error</title>
                          </head>
                          <body style="background-color: #FE2E2E;">
                          <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                          <a href="/"> Main page </a>
                          <hr>
                          <p> Please write a valid human gene </p>
                          </body>
                          </html>"""

                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""

            elif option[0] == ENDPOINTS[6]:
                index = option[1].split("&")
                chromo = index[0].split("=")[1]
                start = index[1].split("=")[1]
                end = index[2].split("=")[1]
                try:
                    conn = SERVER + ext[
                        4] + chromo + ":" + start + "-" + end + '?feature=gene;content-type=application/json'
                    print(conn)
                    connection = requests.get(conn)
                    data = connection.json()
                    u = "<ul>"

                    if len(data) != 0:
                        # for each element in data we will add the genes we want
                        for i in data:
                            u += '<p>' "<li>" + i["external_name"] + "</li>" + "</p>"
                    else:
                        # When the dictionary is empty, it will return the following message
                        u += "Sorry, choose another region"
                    u = u + """</ul></body></html>"""

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: lightcyan;">
                                       <h1><b><FONT face = "Courier New">Gene List</b></FONT></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p>Selected chromosome:  {} <P>
                                       <p>Start: {} </P>
                                       <p>End: {} </P>
                                       <p>Gene List: {} </p>"""
                    # Add it to the html file:
                    contents = contents.format(chromo, start, end, u)

                except TypeError:
                    contents = """<!DOCTYPE html> 
                          <html lang="en"> 
                          <head>
                               <meta charset="UTF-8">
                               <title>Error</title>
                          </head>
                          <body style="background-color: #FE2E2E;">
                          <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                          <a href="/"> Main page </a>
                          <hr>
                          <p> Please enter a valid combination </p>
                          </body>
                          </html>"""
                except IndexError:
                    contents = """<!DOCTYPE html> 
                                          <html lang="en"> 
                                          <head>
                                               <meta charset="UTF-8">
                                               <title>Error</title>
                                          </head>
                                          <body style="background-color: #FE2E2E;">
                                          <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                          <a href="/"> Main page </a>
                                          <hr>
                                          <p> Please enter a valid combination </p>
                                          </body>
                                          </html>"""

                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</b></FONT></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""

            else:
                self.send_response(404)
                with open('Error.html', 'r') as f:
                    for i in f:
                        contents += i
                        contents = str(contents)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # Response message
        self.wfile.write(str.encode(contents))


# Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("serving at port {}".format(PORT))

    try:

        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
