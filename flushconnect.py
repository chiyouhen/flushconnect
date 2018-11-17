#! /usr/bin/env python

import socket
import threading

class Acceptor(threading.Thread):
    def __init__(self, server_addr):
        super(Acceptor, self).__init__()
        self.daemon = True
        self.server_addr = server_addr
        self.connections = []

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(self.server_addr)
        s.listen(128)
        while True:
            c = s.accept()
            self.connections.append(c)

class Connector(threading.Thread):
    def __init__(self, server_addr):
        super(Connector, self).__init__()
        self.server_addr = server_addr
        self.daemon = True
        self.connections = []

    def run(self):
        while True:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect(self.server_addr)
            self.connections.append(c)
            print(len(self.connections))

svr_addr = ('127.0.0.1', 18000)
svr = Acceptor(svr_addr)
svr.start()
cli = Connector(svr_addr)
cli.start()

        
svr.join()
cli.join()            
