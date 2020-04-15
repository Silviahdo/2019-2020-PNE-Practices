from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# -- Client sends 2 messages to the server
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")