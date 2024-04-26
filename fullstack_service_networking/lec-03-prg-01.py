import socket

HOST = '127.0.0.1'
PORT = 65456

print("> echo-server is activated")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    clientSoket, clientAddress = serverSocket.accept()
    with clientSoket:
        print('> client connected by IP address {0} with Port number {1}'.format(clientAddress[0], clientAddress[1]))
        while True:
            #[=start=]
            RecvData = clientSoket.recv(1024)
            print('> echoed:', RecvData.decode('utf-8'))
            clientSoket.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break
            #[==end==]

print('> echo-server is de-activated')