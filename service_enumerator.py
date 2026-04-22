#/usr/bin/env python
import socket

# ServiceEnumerator Class.  Connect to a specific IP and port to retrieve the service
# banner, providing information about the running service.
class ServiceEnumerator:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def get_banner(self):
        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((self.ip, self.port))
            banner = sock.recv(1024).decode().strip()
            sock.close()
            return banner
        except:
            return None
