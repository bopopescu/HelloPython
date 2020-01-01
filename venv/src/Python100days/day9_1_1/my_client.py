from socket import socket

def main():
    client=socket()
    client.connect(('localhost',6868))
    msg=client.recv(1024).decode('utf-8')
    print(msg)
    client.close()

if __name__ == '__main__':
    main()