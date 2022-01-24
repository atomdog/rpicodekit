#switchtrigger.py


import socket
import lightinterface
import subprocess

class centre():
    subprocess.call("huep.py", shell=True)
    def __init__(self):
        #init udp listener
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 6969
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind((UDP_IP, UDP_PORT))
    #check udp for messages
    def check_udp(self):
        data, addr = self.sock.recvfrom(1024)
        return(data, addr)
    def parse_inputs(self, data, addr, switchstate):
        lightinterface.handler(data[0],data[1],data[2],data[3])
        return(True)
    def check_switch(self):
        return(False)
    def run_time(self):
        while(True):
            data, addr = self.check_udp()
            switchstate = self.check_switch()
            self.parse_inputs(data, addr, switchstate)

q = centre()
q.run_time()
