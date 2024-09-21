import socket
import threading

class NetworkArchitecture:
    def __init__(self, protocol, host, port):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(data.encode())

    def receive(self):
        return self.socket.recv(1024).decode()

    def close(self):
        self.socket.close()

class TCPNetworkArchitecture(NetworkArchitecture):
    def __init__(self, host, port):
        super().__init__('tcp', host, port)

    def listen(self):
        self.socket.listen(1)
        connection, address = self.socket.accept()
        return connection

class UDPPacket:
    def __init__(self, data, address):
        self.data = data
        self.address = address

class UDPNetworkArchitecture(NetworkArchitecture):
    def __init__(self, host, port):
        super().__init__('udp', host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data, address):
        self.socket.sendto(data.encode(), address)

    def receive(self):
        data, address = self.socket.recvfrom(1024)
        return UDPPacket(data.decode(), address)

# Example usage
tcp_network_architecture = TCPNetworkArchitecture('localhost', 8080)
tcp_network_architecture.connect()
tcp_network_architecture.send('Hello, server!')
print(tcp_network_architecture.receive())
tcp_network_architecture.close()

udp_network_architecture = UDPNetworkArchitecture('localhost', 8081)
udp_network_architecture.send('Hello, server!', ('localhost', 8081))
packet = udp_network_architecture.receive()
print(packet.data)
