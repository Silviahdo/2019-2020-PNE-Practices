from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

# T1: Ping
print("* Testing PING...")
print(c.talk("PING"))

# T2: Get
print("* Testing GET...")
for i in range(5):
    command = f"GET {i}"
    print(f"{command}: {c.talk(command)}", end="")

# T3: INFO
seq = c.talk("GET 0")
print()
print("* Testing INFO...")
command = f"INFO {seq}"
print(c.talk(command))

# T4: COMP
print(" Testing COMP...")
command = f"COMP {seq}"
print(command, end="")
print(c.talk(command))

# T5: REV
print("* Testing REV...")
command = f"REV {seq}"
print(command, end="")
print(c.talk(command))

# T6: GENE
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    command = f"GENE {gene}"
    print(command)
    print(c.talk(command))
