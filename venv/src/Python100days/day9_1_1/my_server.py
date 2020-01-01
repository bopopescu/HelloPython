from socket import socket, SOCK_STREAM, AF_INET

def main():
    server=socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(('localhost',6868))
    server.listen(512)
    print('Start to listen')
    while True:
        client, addr=server.accept()
        print(str(addr)+'has connected')
        client.send('Hi, this is server'.encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()