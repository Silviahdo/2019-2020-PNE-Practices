from Client0 import Client

PORT = 8080
IP = "192.168.1.45"

for number in range(5):
    c = Client(IP, PORT)
    print("Message", c.debug_talk(number))